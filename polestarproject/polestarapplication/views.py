from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
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

        shiplist = ShipDetail.objects.all()
        serialiazer = ShipDetailSerializer(shiplist, many=True)
        return Response(serialiazer.data)

"""
This class designed to return the position details from the database
param: self, request
"""
class getPositionDetails(APIView):

    def get(self, request, imo):

        trackinglist = ShipPositionDetails.objects.filter(
            imo=imo).order_by('-created_date')
        serialiazer = ShipPositionDetailsSerializer(trackinglist, many=True)
        return Response(serialiazer.data)
