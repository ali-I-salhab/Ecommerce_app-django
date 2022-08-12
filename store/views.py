from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from itertools import product
from multiprocessing import context
from urllib import response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart, CartItem, Collection, Product, Review
from .serializer import CartItemSerialzer, CartSerilaizer, CollectionSerializer, ProductSerialzer, ReviewSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,GenericViewSet

from django.db.models.aggregates import Count
from store import serializer
from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin,RetrieveModelMixin
# here we erplace each fun with a class view 
# that give us a set of reusable things Mixins
class ProductListWithClass(ModelViewSet):
    serializer_class=ProductSerialzer
    queryset=Product.objects.select_related('collection').all()
    def get_context_data(self, **kwargs):
        return {'request' : self.request}

    

    # def get(self ,request):
    #     # RetrieveModelMixin.retrieve(Product,request=request)
    #     queryset=Product.objects.select_related('collection').all()
    #     serializer=ProductSerialzer(queryset,many=True,context={'request':request})
    #     return Response('DAta')


    # def post(self,request):
    #     serializer=ProductSerialzer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

# deserilaizing is opposite of
#  serializing it happens when we recieve data from client
# Create your views here.
#api view decorator
class ProductDetailsWithClass(RetrieveUpdateDestroyAPIView):
    serializer_class=ProductSerialzer
    queryset=Product.objects.all()
    # def get(self,request,id):
    #     product =get_object_or_404(Product,pk=id)
    #     print(product)
    #     print('-----------------')
    #     serializer=ProductSerialzer(product)
    #     #  {'id': 1, 'title': 'Bread Ww Cluster', 'unit_price': '4.00'}
    #     print(serializer.data)
    #     #here we convert product object to py dic
    #     return Response(serializer.data)
    # def put(self,request,id):
    #     product =get_object_or_404(Product,pk=id)

    #     serializer=ProductSerialzer(product,data=request.data,)



    # # add project---> tell us we want to update
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
        

    def delete(self,request,id):
        product =get_object_or_404(Product,pk=id)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






# @api_view(['GET','POST'])
# def product_list(request):
#     if request.method=='GET':
#         print('--------------------get ---------------')
#         #serilaizing
#         #convert product object to python dictionary then to  json object
#         querset=Product.objects.select_related('collection').all()
#         serializer=ProductSerialzer(querset,
#         many=True,context={'request':request})
#         return Response('oh'
#         # data = serializer.data
#             )
#         # here we return json object to user (serializing)

#     elif request.method=='POST':
#         print('--------------------post---------------')

#         serializer=ProductSerialzer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # print(serializer.validated_data)
#         return Response(data= serializer.data)
#         # #deserialising
#         # #here we get json object from user and we want to convert it to class model 
#         # #to save it in dataset
#         # serializer=ProductSerialzer(data=request.data)
#         # if serializer.is_valid():
#         #     serializer.validated_data
#         # #print(serializer.validated_data)
#         #     return Response('ok')
#         # else:
#         #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         # return Response(serializer.data,status=status.HTTP_201_CREATED)
            

#         # else :
#             # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
#         print(serializer)


#         # her deserialize happen 
#         # we get json object we need to convert to model object and save it to database 


# @api_view(['GET','PUT','DELETE'])
# def product_details(request,id):
#     product =get_object_or_404(Product,pk=id)

#     if request.method=='GET':
#         product =get_object_or_404(Product,pk=id)
#         print(product)
#         print('-----------------')
#         serializer=ProductSerialzer(product)
#         #  {'id': 1, 'title': 'Bread Ww Cluster', 'unit_price': '4.00'}
#         print(serializer.data)
#         #here we convert product object to py dict
#         return Response(serializer.data)
#     elif request.method=='PUT':
#         # deserializing the data ,validate and ,save to database 
#         serializer=ProductSerialzer(product,data=request.data,)



#     # add project---> tell us we want to update
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#         # here deserializing 
#         # we also need to pass instance of product to update from data.request
             
#     elif request.method=='DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
   
# @api_view(['GET','POST'])
class collection_list(ModelViewSet):
    serializer_class=CollectionSerializer
    queryset=Collection.objects.all()




    # if request.method=='GET':
    #     queryset=Collection.objects.all()
    #     serializer=CollectionSerializer(queryset,many=True) 
    #     return Response(serializer.data)
    # elif request.method=='POST':
    #     serializer=CollectionSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data,status=status.HTTP_201_CREATED)    


class collection_datils(RetrieveUpdateDestroyAPIView):
    lookup_field='id'
    serializer_class=CollectionSerializer
    queryset=Collection.objects.annotate(product_count=Count('product'))


#we need away to convert product object to Json object 
#render take dict object and return Json object 
# product ---> python dict ---> json dict






#serializer ----> know how to convert a model instance to dictionary

# serializer ---> product ---> python dict 
#render ----> python dict ---> json dict
# class based views 
#function based view 
# we will convert product_list to  class based views 





################################advanced django concepts ######################
# every thing in the view.py was function based view but we can use class based view 





#end_point
#restful
#representational state transfer
#REPRESENTATIONAL STATE TRANSFER
#REST DEFINE SOME RULES TO CONNECT BETWEEN SERVER AND CLIENT

#FASR 
# SCALBLE 
# RELIABLE

#EASY RO UNSERSTANT 
# EASY TO CHANGE 
#
# RESOURCES RESOURCEREPRESENATAION HTTP METHODS #
#RESOURCE IN DJANGO API IS LIKE AN OBJECT LIKE PRODUCT ORDER CUSTOMER AND SOO ON
#UNIFORM RESOURCE LOCATOR 
#RESOURCES CAN BE NESTED
#RESOURCE REPRESENATIONS
#
#HTML XML JSON
#JSON JAVASCRIT OBJECT NOTATION 
#{
# NAME : " "
 # ,AGE :
 # 'IS_ONLINE :[]
 # , SETTING :{}
 # 
 # 
 # # 

# 
# }
#HTTPmETHONS
# GET : GET RESOURCE OR COLLECTION OF RESOURCES 
# PUT : UPDATE RESOURCE 
# POST : CREATING RESOURCE
# PATCH: UPDATE PART OF RESOURCE 
# DELETE:# DELETE RESOURCE 
# **********************************building Apicart???????????????????
class CartViewSet(CreateModelMixin,DestroyModelMixin,RetrieveModelMixin,GenericViewSet):
    serializer_class=CartSerilaizer
    queryset=Cart.objects.all()




class CartItemViewSet(ModelViewSet):
    serializer_class=CartItemSerialzer
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])

class ReviewViewSet(ModelViewSet):
    serializer_class=ReviewSerializer
    queryset=Review.objects.all()