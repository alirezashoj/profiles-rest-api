from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers



class HelloApiView(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializer

    def get(self , request , format=None):
        """returns a list of APIView features"""
        an_apivew = [
            'uses Http methods as function (get , post , patch , put , delete)',
            'is similiar to a traditional django view',
            'Gives you the most controk over you application logic',
        ]

        return Response({'messages' : 'Hello!' , 'an_apivew':an_apivew})

    def post(self , request):
        """"create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self , request , pk = None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request , pk = None):
        """"Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request , pk = None):
        """"delete an object"""
        return Response({'method':'DELETE'})
