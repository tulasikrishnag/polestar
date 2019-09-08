from rest_framework import serializers
from polestarapplication.models import ShipDetail,ShipPositionDetails

class ShipDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model=ShipDetail
		fields='__all__'



class ShipPositionDetailsSerializer(serializers.ModelSerializer):

	class Meta:
		model=ShipPositionDetails
		fields='__all__'