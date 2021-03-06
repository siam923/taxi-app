from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db.models import Q

from .serializers import LogInSerializer, TripSerializer, UserSerializer, NestedTripSerializer
from .models import Trip


class SignUpView(generics.CreateAPIView):
    '''
    Used for creating user with api request
    '''
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LogInView(TokenObtainPairView): # new
    '''
    Used to send login request
    '''
    serializer_class = LogInSerializer


class TripView(viewsets.ReadOnlyModelViewSet):
   lookup_field = 'id'
   lookup_url_kwarg = 'trip_id'
   permission_classes = (permissions.IsAuthenticated,)
   serializer_class = NestedTripSerializer

   def get_queryset(self): # new
       user = self.request.user
       if user.group == 'driver':
           return Trip.objects.filter(
               Q(status=Trip.REQUESTED) | Q(driver=user)
           )
       if user.group == 'rider':
           return Trip.objects.filter(rider=user)
       return Trip.objects.none()