"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.urls.conf import include
## router urls
from first_app.urls import router
from django.conf.urls import url
## swagger API
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Student operation API')

from first_app import views

from rest_framework.authtoken.views import obtain_auth_token
from first_app.views import login_token

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('get_stud/<int:id>/', views.single_student, name= 'get-stud'),
    # path('all_studs/', views.all_students, name= 'all-stud'),
    # path('create_stud/', views.create_data, name= 'create-stud'),
    

    ## single API for all methods

    # path('student_api/', views.student_api, name= 'stud-api'),

    # path('studentapi/', views.student_api, name = 'api'),

    # ## APIView
    # path('studentapiview/', views.StudentAPINew.as_view()),     ## when id is not required, post, get all
    # path('studentapiview/<int:id>/', views.StudentAPINew.as_view()),  

    # ##  mixins and Generic API view---
    # path('s-list/', views.StudList.as_view()),
    # path('s-get/<int:pk>/', views.StudRetrieve.as_view()),
    # path('s-create/', views.StudCreate.as_view()),
    # path('s-update/<int:pk>/', views.StudUpdate.as_view()),
    # path('s-destroy/<int:pk>/', views.StudDestroy.as_view()),

    # ## Concrete Generic API Views

    # path('s-list-c/', views.StudListC.as_view()),
    # path('s-create-c/', views.StudCreateC.as_view()),
    # path('s-retr-c/<int:pk>', views.StudRetrC.as_view()),
    # path('s-upd-c/<int:pk>', views.StudUpdC.as_view()),
    # path('s-dest-c/<int:pk>', views.StudDestrC.as_view()),

    ## view set url router from app.url--
    path('stud/', include(router.urls)),              ## router all urls, stud, college, album, track named as stud


    ### rest-framework- swagger---
    url(r'^$', schema_view), 
    ## session login authentication--- defined rest_framework urls
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),     ##/login, /logout

    ## token generation
    path('api-token/', obtain_auth_token, name = 'api_auth_token'),         ## for default token genration

    path('login-token/', login_token, name= 'auth_token'),

    ## JWT authentication

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    

    ## DRF  filtering
    path('stud-filter/', views.StudListFilterAPI.as_view(), name = "api-filter"),


]
