from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """
    def get(self, request):
        """
        Handle GET requests to return a list of MyModel objects
        """
        my_model = MyModel.objects.all()
        serializer = MyModelSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Handle POST requests to create a new MyModel object
        """
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        """
        Handle PUT requests to update an existing MyModel object
        """
        my_model = MyModel.objects.get(pk=pk)
        serializer = MyModelSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a MyModel object
        """
        my_model = MyModel.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
