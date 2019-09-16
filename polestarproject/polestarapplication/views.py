from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from polestarapplication.models import ShipDetail,ShipPositionDetails
from polestarapplication.serializers import ShipDetailSerializer,ShipPositionDetailsSerializer

"""
This mehtod redirect the user request to index page
params:request
"""
def index(request):
    return render(request, 'index.html')
"""
This class designed to return the list of ship details from the database
param: self, request
"""
class getShipDetails(APIView):

    def get(self, request):
        try:
            shiplist = ShipDetail.objects.all()
            serialiazer = ShipDetailSerializer(shiplist, many=True)
            return Response(serialiazer.data,status=status.HTTP_200_OK)
        except Exception:
            return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)
        

"""
This class designed to return the position details from the database
param: self, request
"""
class getPositionDetails(APIView):

    def get(self, request, imo):
        try:
            trackinglist = ShipPositionDetails.objects.filter(
            imo=imo).order_by('-position_dt_tm')
            serialiazer = ShipPositionDetailsSerializer(trackinglist, many=True)
            return Response(serialiazer.data,status=status.HTTP_200_OK)
        except Exception:
            return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)