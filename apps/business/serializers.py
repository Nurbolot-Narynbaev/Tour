from rest_framework import serializers


from .models import (
    Company,
    Guide
    )

class CompanyCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  

    class Meta:
        model = Company
        exclude = ('slug',)

    def validate(self, attrs):
        author = attrs.get('name')
        if Company.objects.filter(name=author).exists():
            raise serializers.ValidationError(
                'This author already exists'
            )
        user = self.context['request'].user                   
        attrs['user'] = user
        return attrs
    

class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company 
        fields = ['first_name', 'last_name', 'slug', 'user']  


class CompanyRetrieveSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  

    class Meta:
        model = Company
        fields = '__all__'

    def validate(self, attrs):                               
        user = self.context['request'].user
        attrs['user'] = user
        return attrs

class GuideCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  

    class Meta:
        model = Guide
        exclude = ('slug',)

    def validate(self, attrs):
        author = attrs.get('name')
        if Guide.objects.filter(name=author).exists():
            raise serializers.ValidationError(
                'This author already exists'
            )
        user = self.context['request'].user                   
        attrs['user'] = user
        return attrs
    

class GuideListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide 
        fields = ['first_name', 'last_name', 'slug', 'user']  


class GuideRetrieveSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  

    class Meta:
        model = Guide
        fields = '__all__'

    def validate(self, attrs):                               
        user = self.context['request'].user
        attrs['user'] = user
        return attrs