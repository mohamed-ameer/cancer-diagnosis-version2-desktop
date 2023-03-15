from rest_framework import serializers
from cancerDetect.models import CancerDetect
# get put update delete Assignment data
class CancerDetectSerializer(serializers.ModelSerializer):
    class Meta:
        model=CancerDetect
        fields='__all__'
# class CancerDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=CancerDetail
#         fields='__all__'
