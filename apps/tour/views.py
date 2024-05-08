from rest_framework.viewsets import ModelViewSet, GenericViewSet   
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
)   

from .models import (
    Tour,
    Specific_Tour,  
)
from apps.account.permissions import (
    IsOwner
)

from .serializers import (
    TourCreateSerializer, 
    TourListSerializer, 
    TourRetrieveSerializer,
    
    Specific_TourCreateSerializer, 
    Specific_TourListSerializer, 
    Specific_TourRetrieveSerializer,

)

class TourViewSet(ModelViewSet):      
    queryset = Tour.objects.all()
    serializer_class = TourCreateSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return TourCreateSerializer
        elif self.action == 'list':
            return TourListSerializer
        elif self.action == 'retrieve':
            return TourRetrieveSerializer
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
    

class Specific_TourViewSet(ModelViewSet):      # CRUD - Create, Retrieve, Update, Delete, 
    queryset = Specific_Tour.objects.all()
    serializer_class = Specific_TourCreateSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return Specific_TourCreateSerializer
        elif self.action == 'list':
            return Specific_Tour.ListSerializer
     
        elif self.action == 'retrieve':
            return Specific_TourRetrieveSerializer
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
        producer_id = request.query_params.get('producer_id')
        if producer_id:
            queryset = queryset.filter(producer_id=producer_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

