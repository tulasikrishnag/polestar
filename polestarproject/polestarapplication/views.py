from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from polestarapplication.models import ShipDetail,ShipPositionDetails
from polestarapplication.serializers import ShipDetailSerializer,ShipPositionDetailsSerializer
# Create your views here.
from django.http import HttpResponse

def index(request):
	return render(request,'index.html')

class getShipDetails(APIView):

	def get(self, request):

		shiplist= ShipDetail.objects.all();
		serialiazer=ShipDetailSerializer(shiplist,many=True)
		return Response(serialiazer.data)

class getPositionDetails(APIView):

	def get(self, request,imo):

		trackinglist= ShipPositionDetails.objects.filter(imo=imo).order_by('-id');
		serialiazer=ShipPositionDetailsSerializer(trackinglist,many=True)
		return Response(serialiazer.data)
