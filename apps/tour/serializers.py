from rest_framework import serializers


from .models import (
    Tour,
    Tour_Image,
    Specific_Tour
    )

class TourCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')   

    class Meta:
        model = Tour
        exclude = ('slug',)

    def validate(self, attrs):
        tour = attrs.get('title')
        if Tour.objects.filter(title=tour).exists():
            raise serializers.ValidationError(
                'This tour already exists'
            )
        user = self.context['request'].user                   
        attrs['user'] = user
        return attrs
    

class TourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour 
        fields = ['title', 'user', 'company_name']  


class TourRetrieveSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  

    class Meta:
        model = Tour
        fields = 'all'

    def validate(self, attrs):                               
        user = self.context['request'].user
        attrs['user'] = user
        return attrs    


class Specific_TourCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  

    class Meta:
        model = Specific_Tour
        exclude = ('slug',)

    def validate(self, attrs):
        specific_Tour = attrs.get('tour')
        if Specific_Tour.objects.filter(tour=specific_Tour).exists():
            raise serializers.ValidationError(
                'This author already exists'
            )
        user = self.context['request'].user                   
        attrs['user'] = user
        return attrs
    

class Specific_TourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specific_Tour 
        fields = ['first_name', 'last_name', 'slug', 'user', 'company']  


class Specific_TourRetrieveSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  

    class Meta:
        model = Specific_Tour
        fields = 'all'

    def validate(self, attrs):                               
        user = self.context['request'].user
        attrs['user'] = user
        return attrs
class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour_Image
        
        fields = 'image', 