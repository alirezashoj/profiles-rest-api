from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """"Test API view"""

    def get(self , request , format = None):
        """returns a list of APIView features"""
        an_apivew = [
            'uses Http methods as function (get , post , patch , put , delete)',
            'is similiar to a traditional django view',
            'Gives you the most controk over you application logic',
        ]

        return Response({'messages' : 'Hello!' , 'an_apivew':an_apivew})
