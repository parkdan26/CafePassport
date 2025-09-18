# cafes/serializers.py
from rest_framework import serializers
from .models import Cafe, PassportCafe

class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = ['id', 'name', 'address', 'city', 'description', 'logo']


class PassportCafeSerializer(serializers.ModelSerializer):
    cafe = CafeSerializer(read_only=True)
    cafe_id = serializers.PrimaryKeyRelatedField(
        queryset=Cafe.objects.all(), source='cafe', write_only=True
    )

    class Meta:
        model = PassportCafe
        fields = ['id', 'cafe', 'cafe_id', 'rating', 'bio', 'added_at']
