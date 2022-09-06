from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from departments.models import Department
from departments.serializers import DepartmentSerializer


@csrf_exempt
def department_list(request):
    """
    List all departments, or create a new department.
    """
    if request.method == "GET":
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def department_detail(request, pk):
    """
    Retrieve, update or delete a department.
    """
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = DepartmentSerializer(department)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(department, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        department.delete()
        return HttpResponse(status=204)
