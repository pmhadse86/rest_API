from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from first_app.models import Student, College, Album, Track

from first_app.serializers import StudentSerializer,CollegeSerializer, AlbumSerializer, TrackSerializer

import io
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer               ## serializer
from rest_framework.parsers import  JSONParser                       ## deserializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Create your views here.

"""
def single_student(request, id):
        stud_obj = Student.objects.get(id= id)                      ## complex data
        print(stud_obj)
        python_obj = StudentSerializer(stud_obj)                         ## complex data to native python       
        json_data = JSONRenderer().render(python_obj.data)              ## json data     
        return HttpResponse(json_data, content_type= 'application/json')
        # return HttpResponse("Welcome to student board")

def all_students(request):
        studs = Student.objects.all()
        python_obj = StudentSerializer(studs, many = True)
        json_data = JSONRenderer().render(python_obj.data)
        return HttpResponse(json_data, content_type=  "application/json") 

### post requests

import io

@csrf_exempt
def create_data(request):
        if request.method == 'POST':
                byte_data = request.body                    ## json data
                streamed_data = io.BytesIO(byte_data)
                python_data = JSONParser().parse(streamed_data)              ## python data
                print(python_data)
                ser = StudentSerializer(data = python_data)
                if ser.is_valid():
                        ser.save()
                        msg = {"msg" : "Data saved to database successfully"}
                        res=  JSONRenderer().render(msg)
                # print(ser)
                return HttpResponse(res, content_type = 'application/json')
                # return HttpResponse("Data saved successfully")

        else:
                return HttpResponse("only Post request")

##########student API......   all methods--------------

@csrf_exempt

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
        if request.method == "GET":
                byte_data = request.body                # json data
                streamed_data = io.BytesIO(byte_data)
                python_data = JSONParser().parse(streamed_data)         ## {"id" :1}
                
                sid = python_data.get("id")
                if sid:                                                 # single data for id
                        stud = Student.objects.get(id = sid)
                        ser = StudentSerializer(stud)
                        # json_data = JSONRenderer().render(ser.data)
                        # return HttpResponse(json_data, content_type= 'apllication/json')
                        return JsonResponse(ser.data)

                else:                                                   # for all
                        studs = Student.objects.all()
                        ser = StudentSerializer(studs, many = True)
                        # json_data = JSONRenderer().render(ser.data)
                        # return HttpResponse(json_data, content_type = 'application/json')
                        return JsonResponse(ser.data, safe= False)

        elif request.method == "POST":  
                # data1 = request.data                         ### python data         
                # # print(data1)                             # python dict data
                # ser = StudentSerializer(data = data1)
                data_bytes = request.body
                stream_data = io.BytesIO(data_bytes)
                python_data = JSONParser().parse(stream_data)
                ser = StudentSerializer(data = python_data)
                if ser.is_valid():
                        ser.save()
                        return JsonResponse({"msg" : " Data saved to database"})
                return JsonResponse({"error" : "invalid data"})


        elif request.method == "PUT":
                data_bytes = request.body                       ## json data dict
                stream_data = io.BytesIO(data_bytes)
                python_data = JSONParser().parse(stream_data)
                sid = python_data.get("id")
                if sid:
                        stud = Student.objects.get(id= sid)             # existing data from DB
                ser = StudentSerializer(instance= stud, data= python_data)      # instance is stud obj
                if ser.is_valid():
                        ser.save()
                        return JsonResponse({"msg": "data updated successfully"})

        elif request.method == "DELETE":
                data_bytes = request.body                       ## json data dict
                stream_data = io.BytesIO(data_bytes)
                python_data = JSONParser().parse(stream_data)
                
                sid = python_data.get("id")
                if sid:
                        stud = Student.objects.get(id = sid)
                        stud.delete()
                        return JsonResponse({"msg": "data deleted successfully"})
                        

        else:
                msg ={"msg" : "Invalid request method "}
                res = JSONRenderer().render(msg)
                return HttpResponse(res, content_type = 'application/json')

"""

###   class based views-------------

# from django.views import View

# class Studentview(View):
#         def get(self, request, *args, **kwargs):
#                 pass

#         def get(self, request, *args, **kwargs):
#                 pass

#         def get(self, request, *args, **kwargs):
#                 pass

#         def get(self, request, *args, **kwargs):
#                 pass

import io
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


### API view with functions

@api_view(['GET' , 'POST' , 'PUT' , 'DELETE' ])

def student_api(request):
        if request.method == 'GET':
                sid = request.data.get('id')
                if sid:
                        stud = Student.objects.get(id= sid)
                        ser = StudentSerializer(stud)
                        return Response(ser.data)
                else:
                        studs = Student.objects.all()
                        ser= StudentSerializer(studs, many= True)
                        return Response(ser.data)

        elif request.method == 'POST':
                data1 = request.data
                ser = StudentSerializer(data= data1)
                print(ser)
                if ser.is_valid():
                        ser.save()
                        return Response({'msg': 'Data saved'})
                else:
                        return Response(ser.errors)

        elif request.method == 'PUT':
                python_data = request.data
                sid = python_data.get("id")
                stud = Student.objects.get(id = sid)
                ser = StudentSerializer(instance= stud, data = python_data, partial= True)
                if  ser.is_valid():
                        ser.save()
                        return Response({'msg': 'Data saved'})
                else:
                        return Response(ser._errors)

        elif request.method == "DELETE":
                python_data = request.data
                sid = python_data.get("id")
                stud = Student.objects.get(id = sid)
                print(stud)
                stud.delete()
                return Response({'msg': 'Data deleted'})



### API view with classes
from rest_framework.decorators  import APIView

class StudentAPINew(APIView):
        def get(self, request, pk = None, format= None):
                sid = pk
                if sid:
                        stud = Student.objects.get(id= sid)
                        ser =  StudentSerializer(stud)
                        return Response(ser.data)
                else:
                        studs = Student.objects.all()
                        ser = StudentSerializer(studs, many= True)
                        return Response(ser.data)
                        
        def post(self, request,  format= None):
                data1 = request.data
                print(data1)
                ser = StudentSerializer(data= data1)
                if ser.is_valid():
                        ser.save()
                        return Response({'msg': 'Data saved', 'data': request.data})
                return response(ser.errors)

        def put(self, request, pk, format= None):
                sid= pk
                if sid:
                        stud = Student.objects.get(id= sid)
                        ser = StudentSerializer(instance= stud, data= request.data)
                        if ser.is_valid():
                                ser.save()
                                return Response({'msg': 'Data Updated', "data": request.data})

                        return response(ser.errors)

        def patch(self, request, pk, format= None):
                sid= pk
                if sid:
                        stud = Student.objects.get(id= sid)
                        ser = StudentSerializer(instance= stud, data= request.data, partial = True)
                        if ser.is_valid():
                                ser.save()
                                return Response({'msg': 'Partial data Updated', "data": request.data})
                        return response(ser.errors)


        def delete(self, request, pk, format= None):                    ## Soft delete
                sid = pk
                stud = Student.objects.get(id= sid)
                stud.delete()
                return Response({'msg': 'Data deleted'})

#########-----------Generic API------- mixins-----------------------

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

class StudList(GenericAPIView, ListModelMixin):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer            ## for generic view

        def get(self, request, *args, **kwargs):
                return self.list(self, request, *args, **kwargs)

class StudRetrieve(GenericAPIView, RetrieveModelMixin):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer 

        def get(self, request, *args, **kwargs):
                return self.retrieve(self, request, *args, **kwargs)

class StudCreate(GenericAPIView, CreateModelMixin):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer 

        def post(self, request, *args, **kwargs):
                return self.create(request, *args, **kwargs)

class StudUpdate(GenericAPIView, UpdateModelMixin):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer 

        def put(self, request, *args, **kwargs):
                return self.update(request, *args, **kwargs)


class StudDestroy(GenericAPIView, DestroyModelMixin):

        queryset = Student.objects.all()
        serializer_class = StudentSerializer 
        
        def delete(self, request, *args, **kwargs):
                return self.destroy(request, *args, **kwargs)


######   Concrete Generic API View classes----

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

class StudListC(ListAPIView):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer

class StudCreateC(CreateAPIView):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
        
class StudRetrC(RetrieveAPIView):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer

class StudUpdC(UpdateAPIView):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
        
class StudDestrC(DestroyAPIView):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
        

###  View Sets------------

## provides--- list(), create(), retrieve(), update() methods
##  url routers... to automatically route urls

from rest_framework.viewsets import ViewSet

class StudentViewSet(ViewSet):
        def list(self, request):
                studs = Student.objects.all()
                ser = StudentSerializer(studs, many =True)
                return Response(ser.data)

        def create(self, request):
                data1 = request.data
                ser = StudentSerializer(data1)
                if ser.is_valid():
                        ser.save()
                        return Response(ser.data, status= status.HTTP_201_CREATED)
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        def retrieve(self, request, pk):
                sid = pk
                stud = Student.objects.get(id = sid)
                ser = StudentSerializer(stud)
                return Response(ser.data, status= status.HTTP_302_FOUND)

        def update(self, request, pk):
                sid = pk
                stud = Student.objects.get(id = sid)
                ser = StudentSerializer(instance =stud, data= request.data)
                if ser.is_valid():
                        ser.save()
                        return Response(ser.data, status=status.HTTP_200_OK)
                return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

        def partial_update(self, request, pk):
                sid = pk
                stud = Student.objects.get(id = sid)
                ser = StudentSerializer(instance =stud, data= request.data, partial= True)
                if ser.is_valid():
                        ser.save()
                        return Response(ser.data, status=status.HTTP_200_OK)
                return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        

        def delete(self, request, pk):
                sid = pk
                stud = Student.objects.get(id= sid)
                stud.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
                
###  Model View Sets------------Inherits from APIView, Gneneric View, mixins

# from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

# class StudentModelViewSet(ModelViewSet):                ## all CRUD operations
#         queryset = Student.objects.all()
#         serializer_class = StudentSerializer


####   Authentication.........................

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication 
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class StudentModelViewSet(ModelViewSet):                ## all CRUD operations
        # queryset = Student.objects.all()
        queryset = Student.objects.all().filter(is_deleted= 0)
        serializer_class = StudentSerializer
        # lookup_field = 'name'                                                    ## search by name instead of id/ default is id

        # authentication_classes = [BasicAuthentication]
        # permission_classes = [AllowAny]                             ## all access
        # permission_classes = [IsAuthenticated]                     ## ask for admin credentials
        # permission_classes = [IsAdminUser]                         ##  for superuser and / is_staff allowed
        
        # authentication_classes = [SessionAuthentication]       # for session auth, define new url
        # permission_classes= [IsAuthenticated]
        
        # # ----------------------------------  token authentication ----------------------------------------------
        # # ------------------------------  in postman-- Authorization Token token_no.. to activate token------
        
        # authentication_classes = [TokenAuthentication]          ## demands for token, add RF token app in app
        # permission_classes = [ IsAuthenticated] 

        def destroy(self, request, *args, **kwargs):            ## overridden method from destroy mixxin
                instance = self.get_object()
                instance.is_deleted = 1
                instance.save()
                # print(instance, " in destroy")
                return Response(status=status.HTTP_204_NO_CONTENT)

        ## define new func and url for is_deleted data show
        @action(methods=['get'], detail=False, url_path='get-deleted-data', url_name='deleted-data')
        def get_favorite_post(self, request):
                queryset = Student.objects.all().filter(is_deleted= 1)
                ser = StudentSerializer(queryset, many =True)
                return Response(ser.data)

### ------------------------  token generation at user end after userid/password manually-----------

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))                ## for function based
def login_token(request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
                return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
                return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,},  status=HTTP_200_OK)

############- --------------------   ----------------------------

class CollegeModelViewSet(ModelViewSet):
        queryset = College.objects.all()
        serializer_class = CollegeSerializer
        # authentication_classes = [BasicAuthentication]                ## added in settings
        # permission_classes = [IsAuthenticated]                          ## ask for admin credentials
        authentication_classes = [SessionAuthentication]             # for session auth, define new url
        permission_classes= [IsAuthenticated]


#############  FILTERING----------------
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
## pagination

class StudPagination(PageNumberPagination):
        page_size = 5
        page_size_query_param = 'page_size'
        # max_page_size = 1000

class StudListFilterAPI(ListAPIView):
        queryset =  Student.objects.all()
        serializer_class = StudentSerializer
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['id', 'name', 'marks']
        search_fields= ["id", "name"]

        pagination_class = StudPagination
        
        # authentication_classes = [BasicAuthentication]
        # permission_classes = [IsAuthenticated]

        # def get_queryset(self):
        #         return Student.objects.all().filter(city ='Mumbai')

        # def get_queryset(self):
        #         user = self.request.user
        #         return Student.objects.filter(created_by = user.id)
        

### Album/ Track ModelViewSet   ------    Serializer relations

class AlbumModelViewSet(ModelViewSet):
        queryset = Album.objects.all()
        serializer_class = AlbumSerializer

class TrackModelViewSet(ModelViewSet):
        queryset = Track.objects.all()
        serializer_class = TrackSerializer








