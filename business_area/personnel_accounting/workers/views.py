from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from workers.models import Worker
from workers.serializers import WorkerSerializer


@api_view(['GET', 'POST'])
def workers_list(request):
    """
    List all workers, or create a new worker.
    """
    if request.method == "GET":
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def workers_detail(request, pk):
    """
    Retrieve, update or delete a worker.
    """
    try:
        worker = Worker.objects.get(pk=pk)
    except Worker.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = WorkerSerializer(worker)
        result = serializer.data
        # result['workers_count'] = Worker.objects.filter(department=department).count()
        return Response(result)

    elif request.method == "PUT":
        serializer = WorkerSerializer(worker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        worker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
