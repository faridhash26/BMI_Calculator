from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated

from .filters import BMIInfoFilter
from .models import UserBmiInfo
from .serializers import CreateBMIInfoSerializer, ResponseCreateBMIInfoSerializer

# Create your views here.


class BmiView(CreateAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = CreateBMIInfoSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        bmi = self.perform_create(serializer)
        response_serializer = ResponseCreateBMIInfoSerializer(instance=bmi)
        headers = self.get_success_headers(response_serializer.data)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class BmiListView(ListAPIView):
    serializer_class = ResponseCreateBMIInfoSerializer
    filterset_class = BMIInfoFilter
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return UserBmiInfo.objects.filter(user=self.request.user)
