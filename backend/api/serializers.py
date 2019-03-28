from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
	class  Meta:
		model = Review
		fields = ('date','sku','rating','title', 'author', 'text','source')

