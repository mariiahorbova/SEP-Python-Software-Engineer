from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from departments.models import Department
from departments.serializers import DepartmentSerializer
from workers.models import Worker


@api_view(['GET', 'POST'])
def department_list(request):
    """
    List all departments, or create a new department.
    """
    if request.method == "GET":
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def department_detail(request, pk):
    """
    Retrieve, update or delete a department.
    """
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DepartmentSerializer(department)
        result = serializer.data
        result['workers_count'] = Worker.objects.filter(department=department).count()
        return Response(result)

    elif request.method == "PUT":
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
