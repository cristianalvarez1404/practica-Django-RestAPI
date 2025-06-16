from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import PeopleSerializer,LoginSerializer
from rest_framework.views import APIView
from rest_framework import viewsets

@api_view(['GET','POST','PUT'])
def index(request):

  if request.method == 'GET':
    json_response = {
      'name':'Scaler',
      'courses':['C++','Python'],
      'method':'GET'
    }
    
    return Response(json_response)
  else:
    data = request.data
    json_response = {
      'name':'Scaler',
      'courses':['C++','Python'],
      'method':'GET'
    }
    
    return Response(json_response)
  
@api_view(['POST'])
def login(request):
  data = request.data
  serializer = LoginSerializer(data=data)

  if serializer.is_valid():
    data = serializer.validated_data
    return Response({'message':'success'})
    
  return Response(serializer.errors)
  
class PersonAPI(APIView):
  def get(self, request):
    objs = Person.objects.filter(color__isnull=False)
    serializer = PeopleSerializer(objs, many = True)
    return Response(serializer.data)
  
  def post(self,request):
    data = request.data
    serializer = PeopleSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)

  def put(self,request):
    data = request.data
    serializer = PeopleSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    
    return Response(serializer.data)

  def patch(self,request):
    data = request.data
    obj = Person.objects.get(id=data['id'])
    serializer = PeopleSerializer(obj, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    
    return Response(serializer.data)

  def delete(self,request):
    data = request.data
    obj = Person.objects.get(id=data['id'])
    obj.delete()
    return Response({"message":"person deleted"})

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def people(request):
  if request.method == 'GET':
    # objs = Person.objects.all()
    objs = Person.objects.filter(color__isnull=False)
    serializer = PeopleSerializer(objs, many = True)
    return Response(serializer.data)

  elif request.method == 'POST':
    data = request.data
    serializer = PeopleSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
    
  elif request.method == 'PUT':
    data = request.data
    serializer = PeopleSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    
    return Response(serializer.data)
  
  elif request.method == 'PATCH':
    data = request.data
    obj = Person.objects.get(id=data['id'])
    serializer = PeopleSerializer(obj, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    
    return Response(serializer.data)
  
  else:
    data = request.data
    obj = Person.objects.get(id=data['id'])
    obj.delete()
    return Response({"message":"person deleted"})
  
class PeopleViewSet(viewsets.ModelViewSet):
  serializer_class = PeopleSerializer
  queryset = Person.objects.all()

  def list(self,request):
    search = request.GET.get('search')
    queryset = self.queryset

    if search:
      queryset = queryset.filter(name__startwith = search)

    serializer = PeopleSerializer(queryset,many=True) 
    return Response({'status':200,'data':serializer.data})



