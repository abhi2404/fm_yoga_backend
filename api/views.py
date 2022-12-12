import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from api.models import PaymentStatus, Shifts, Userdetails
from rest_framework.permissions import IsAuthenticated
from api.serializers import PaymentHistorySerializer, PaymentSerializer, RegistrationSerializer, ShiftSerializer, UserData
# Create your views here.

def get_month_cycle():      # Function to get current month cycle. For example 11/2022
    today = datetime.datetime.now()
    month = today.month
    year = today.year
    return str(month)+'/'+str(year)


class Registration(APIView):        # API for registration of the user

    def post(self, request):
        if User.objects.filter(username=request.data['username']).exists():
            return Response({'msg':'Username Already Exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(request.data['username'], request.data['email'], request.data['password'])
        user.first_name = request.data['fname']
        user.last_name = request.data['lname']
        user.save()
        request.data['user'] = user.id      # It will initialize the id of the user to request.data so we can use this id for foreign key
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Registration Succesfull'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class user_details(APIView):        # API to get details of the user logged-in
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user.id
        print(user)
        user_data  = Userdetails.objects.get(user=user)
        serializer = UserData(user_data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Login(APIView):       # API to login user with his username and password
    
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        print(request.data['username'],request.data['password'])
        if user is not None:
            login(request, user)
            return Response({'msg':'Login Successfull'}, status=status.HTTP_200_OK)
        return Response({'msg':'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class payment_month_wise(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):        # To pay the amount of the yoga classes of that particular month
        request.data['month_cycle'] = get_month_cycle()     # Get the current month and year
        if PaymentStatus.objects.filter(month_cycle=request.data['month_cycle'], user=request.user.id).exists():       # To check whether the user has already paid the amount for current month or not 
            return Response({'msg':'Payment already done for the current month'}, status=status.HTTP_400_BAD_REQUEST)
        today = datetime.date.today()
        born = list(Userdetails.objects.filter(user=request.user.id).values('dob'))[0]['dob']       # Get date of birth of the user
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))      # Calculating his/her age
        if age<18 or age>65:
            return Response({'msg':'You need to be minimum 18 years old or 65 years old'}, status=status.HTTP_400_BAD_REQUEST)
        request.data['user'] = request.user.id
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Payment Succesfull'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):     # It will return the payment history of the user
        user = request.user.id
        payment_details = PaymentStatus.objects.filter(user=user).order_by('-payment_time')
        serializer = PaymentHistorySerializer(payment_details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class plan_activity(APIView):       # To check whether the user has his plan active or not
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user.id
        month_cycle = get_month_cycle()
        payment=0
        if PaymentStatus.objects.filter(month_cycle=month_cycle, user=user).exists():
            payment = 1
        return Response({'payment':payment}, status=status.HTTP_200_OK)
        

class get_all_shift(APIView):       # It will return all the shift available in yoga classes
    permission_classes = [IsAuthenticated]

    def get(self, request):
        shift = Shifts.objects.all()
        serializer = ShiftSerializer(shift, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Logout(APIView):      # API to logout
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response({'msg':'Logout Succesfull'}, status=status.HTTP_200_OK)