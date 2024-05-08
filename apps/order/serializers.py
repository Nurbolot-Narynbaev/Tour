from rest_framework import serializers

from .models import (
    Order, 
    Order_Items
    )


class Order_ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Items
        fields = ['tour', 'tour_num']


class TourPurchaseSerializer(serializers.ModelSerializer):
    items = Order_ItemsSerializer(many=True) 

    class Meta:
        model = Order_Items
        fields = ['order_id', 'created_at', 'total_sum', 'items']

    def create(self, validated_data, *args, **kwargs):
        items = validated_data.pop('items')
        validated_data['user'] = self.context['request'].user
        order = super().create(validated_data) 
        total_sum = 0
        orders_items = []

        for item in items:
            tickets = (Order_Items(
                order=order,
                tour=item['tour'],
                tour_num=item['tour_num']
            ))
            orders_items.append(tickets)

            if item['tour'].tour_count >= item['tour_num']:
                item['tour'].tour_count -= item['tour_num']

                total_sum += item['tour'].price_som * item['tour_num']
                
                Order_Items.objects.bulk_create(orders_items, *args, **kwargs)
                order.total_sum = total_sum

                # order.create_code() ###
                item['tour'].save()
                order.save()

                return order
            else:
                raise serializers.ValidationError('We do not have so many tour')
    

class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id', 'total_sum', 'status', 'created_at', 'tour')