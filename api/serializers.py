from rest_framework import serializers
from api.models import PaymentStatus, Shifts, Userdetails

class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Userdetails
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentStatus
        fields = '__all__'

class PaymentHistorySerializer(serializers.ModelSerializer):
    shift = serializers.CharField(source='shift.shift')

    class Meta:
        model = PaymentStatus
        exclude = ['id','user']

class UserData(serializers.ModelSerializer):

    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Userdetails
        exclude = ['user', 'registration_timestamp']

class ShiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shifts
        fields = '__all__'