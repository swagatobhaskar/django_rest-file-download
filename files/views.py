import os
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.conf import settings

# @api_view(['GET'])

class DispositionView(APIView):

    def get(self, request, format=None):
        # Define the full file path
        myFile = os.path.join(settings.BASE_DIR, "lorem-ipsum.txt")
        # Open the file for reading content
        path = open(myFile, 'r')
        response = Response(path, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="lorem-ipsum.txt"'

        return response