from home.views import index,people,login,PersonAPI,PeopleViewSet,RegisterAPI,LoginAPI
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people',PeopleViewSet,basename='people')
urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('register/',RegisterAPI.as_view()),
    path('login/',LoginAPI.as_view()),
    path('index/', index),
    path('person/',people),
    path('login/',login),
    path('persons/',PersonAPI.as_view())
]

