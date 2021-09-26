
### ------------    urls for ViewSet

from rest_framework.routers import DefaultRouter
from first_app import views

router = DefaultRouter()

# router.register(r'student-op', views.StudentViewSet, basename='student')      ## ViewSet
router.register(r'student-op', views.StudentModelViewSet, basename='student')        ## ModelViewSet
# router.register(r'college-op', views.CollegeModelViewSet, basename='college' )
router.register(r'album-op', views.AlbumModelViewSet, basename='album')
router.register(r'track-op', views.TrackModelViewSet, basename='track')


# for i in router.urls:
#         print(i)


# <URLPattern '^student-op/$' [name='student-list']>
# <URLPattern '^student-op\.(?P<format>[a-z0-9]+)/?$' [name='student-list']>
# <URLPattern '^student-op/(?P<pk>[^/.]+)/$' [name='student-detail']>
# <URLPattern '^student-op/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='student-detail']>
# <URLPattern '^$' [name='api-root']>
# <URLPattern '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']>