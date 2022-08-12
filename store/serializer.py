
from curses import meta
from dataclasses import field, fields
from decimal import Decimal
from pyexpat import model
from typing import ItemsView


from rest_framework import serializers
from .models import Cart, CartItem, Product,Collection, Review

# here we ditect what fields we want to add to python dictionary 
class CollectionSerializer(serializers.ModelSerializer):
    # id =serializers.IntegerField()
    # title=serializers.CharField(max_length=255)
    class Meta:
        
        model=Collection
        fields='__all__'
      

class ProductSerialzer(serializers.ModelSerializer):
     class Meta:
        model=Product
        fields=['id','title','slug','inventory','unit_price','collection']
    #  def create(self, validated_data):
    #     product =Product(**validated_data)
    #     product.other=1
    #     product.save()
    #     return product
    #     return super().create(validated_data)
    #  def update(self, instance, validated_data):
    #     instance.unit_price =validated_data.get('unit_price')
    #     instance.save()
    #     return instance
         

    # id=serializers.IntegerField()
    # title=serializers.CharField(max_length=255)
    
    # price_with_tax=serializers.SerializerMethodField()
    # unit_price=serializers.DecimalField(max_digits=6,decimal_places=2)
    # price_with_tax=serializers.SerializerMethodField(method_name='calculate_tax')
    # def calculate_tax(self,product:Product):
    #     return product.unit_price*Decimal(1.1)

    # # collection =CollectionSerializer()
    # # collection=serializers.PrimaryKeyRelatedField(
    # #     queryset=Collection.objects.all()
    # # )
    # # collection=serializers.StringRelatedField()
    # collection=serializers.HyperlinkedRelatedField(
    #  view_name='collection_datils',queryset=Collection.objects.all()

    # )
#serializer convert product object to python dictionary    


# {
# "title" : "a",
# "slug" : "a",
# "unit_price" : 1,
# "collection" :1,
# "inventory" : 1

# }




# ***************

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= Review
        fields=['id','date','name','description','product']








    
class SimpleProductSerlaizer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','title','unit_price']

class CartItemSerialzer(serializers.ModelSerializer):
    product=SimpleProductSerlaizer()
    total_price=serializers.SerializerMethodField()
    def get_total_price(self ,cart_item : CartItem):
        return cart_item.quantity*cart_item.product.unit_price
    class Meta:
        model=CartItem
        fields=['id','quantity','product','total_price']

class CartSerilaizer(serializers.ModelSerializer):
    id=serializers.UUIDField(read_only=True)
    items=CartItemSerialzer(many=True,read_only=True)
    total_cart_price=serializers.SerializerMethodField()
    def get_total_cart_price(self,cart):
       return sum([item.quantity*item.product.unit_price for item in cart.items.all()])

    
    class Meta:
        model =Cart
        fields=['id','items','total_cart_price']