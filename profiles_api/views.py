from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self,request, format=None):
        """Returns a list of APIViews features"""
        an_apiview = [
            'Uses HTTP methods as a function(get,post,put,delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped to the URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
            #convert is to .json needs to be lists or dict
