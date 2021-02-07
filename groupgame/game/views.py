from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(APIView):

    def get(self, request):
        return Response({'message': 'Home View'}, status=status.HTTP_200_OK)

class GameView(APIView):

    def post(request):
        return Response({'message': 'GameView'},status=status.HTTP_200_OK)