# Importing necessary Django REST framework modules
from rest_framework import generics, response, status
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist

# Importing the SimpleCRUD model and serializer
from .models import SimpleCRUD
from .serializers import SimpleCRUDSerializer

# List View: Handles GET requests to retrieve all records
class SimpleCRUDList(generics.ListAPIView):

    # Querying all objects from the database
    queryset = SimpleCRUD.objects.all()

    # Specifying the serializer class
    serializer_class = SimpleCRUDSerializer

    # Ensuring only authenticated users can access this view
    permission_classes = (IsAuthenticated, )

    # Overriding the GET method
    def get(self, request):

        # Fetching the filtered queryset
        queryset = self.get_queryset()

        # Serializing the data
        serializer = self.get_serializer(queryset, many=True)

        # Returning the serialized data with HTTP 200 OK status
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
# Detail View: Handles GET requests to retrieve a single record by its ID
class SimpleCRUDDetail(generics.RetrieveAPIView):

    queryset = SimpleCRUD.objects.all()
    serializer_class = SimpleCRUDSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk):

        try:
            # Retrieving and serializing the object with the given primary key (pk)
            serializer = self.serializer_class(self.queryset.get(pk=pk), many=False)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        
        except:
            # Returning an error message if the object does not exist
            return response.Response(data="Object not found", status=status.HTTP_200_OK)
        
# Create View: Handles POST requests to create a new record
class SimpleCRUDCreate(generics.CreateAPIView):

    queryset = SimpleCRUD.objects.all()
    serializer_class = SimpleCRUDSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):

        # Serializing the incoming request data
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # Saving the object to the database if valid
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        else: 
            # Returning validation errors if the data is invalid
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# Update View: Handles PUT requests to update an existing record
class SimpleCRUDUpdate(generics.RetrieveUpdateAPIView):

    queryset = SimpleCRUD.objects.all()
    serializer_class = SimpleCRUDSerializer
    permission_classes = (IsAuthenticated, )

    def put(self, request, pk):

        # Retrieving the object to update
        obj = self.queryset.get(pk=pk)

        # Serializing and validating the updated data
        serializer = self.serializer_class(obj, data=request.data)

        if serializer.is_valid():
            # Saving the updated object
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            # Returning validation errors if the data is invalid
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete View: Handles DELETE requests to remove a record
class SimpleCRUDDelete(generics.RetrieveDestroyAPIView):

    queryset = SimpleCRUD.objects.all()
    serializer_class = SimpleCRUDSerializer
    permission_classes = (IsAuthenticated, )

    def delete(self, request, pk):

        try:
            # Retrieving the object to delete
            obj = self.queryset.get(pk=pk)

            # Deleting the object
            obj.delete()

            # Returning a successful deletion response
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        
        except ObjectDoesNotExist:
            # Returning an error response if the object does not exist
            return response.Response({"error" : "The object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            # Handling unexpected errors during deletion
            return response.Response({"error": "An error occurred while deleting"}, status=status.HTTP_400_BAD_REQUEST)
