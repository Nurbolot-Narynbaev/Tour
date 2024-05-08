from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet , ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from apps.account.permissions import IsOwner

from .models import (
    Company,
    Guide
)
# from .permissions import IsOwner
from .serializers import (
    GuideListSerializer,
    GuideCreateSerializer,
    GuideRetrieveSerializer,
    CompanyRetrieveSerializer,
    CompanyCreateSerializer,
    CompanyListSerializer

    )

User = get_user_model()

class CompanyViewSet(ModelViewSet):      
    queryset = Company.objects.all()
    serializer_class = CompanyCreateSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CompanyCreateSerializer
        elif self.action == 'list':
            return CompanyListSerializer
        elif self.action == 'retrieve':
            return CompanyRetrieveSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == 'list': 
            self.permission_classes = [AllowAny]
        elif self.action == 'retrieve': 
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['create', 'update', 'partial_update']: 
            self.permission_classes = [IsAdminUser]
        elif self.action == 'destroy': 
            self.permission_classes = [IsOwner]
        return super().get_permissions()
    

class GuideViewSet(ModelViewSet):      # CRUD - Create, Retrieve, Update, Delete, 
    queryset = Guide.objects.all()
    serializer_class = GuideCreateSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return GuideCreateSerializer
        elif self.action == 'list':
            return GuideListSerializer
        elif self.action == 'retrieve':
            return GuideRetrieveSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == 'list': 
            self.permission_classes = [AllowAny]
        elif self.action == 'retrieve': 
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['create', 'update', 'partial_update']: 
            self.permission_classes = [IsAdminUser]
        elif self.action == 'destroy': 
            self.permission_classes = [IsOwner]
        return super().get_permissions()
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        author_id = request.query_params.get('author_id')
        if author_id:
            queryset = queryset.filter(author_id=author_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)