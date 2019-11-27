from rest_framework import serializers
from .models import contact

class ContactSerializer(serializers.ModelSerializer):

	class Meta:
		model = contact
		fields = ('name','number','email','spam')



