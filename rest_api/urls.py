from django.conf.urls import url, include
from .views import AlbumViewset, SizeViewset, BindingViewset, TemplateViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('album', AlbumViewset, basename='album')
router.register('size', SizeViewset, basename='size')
router.register('binding', BindingViewset, basename='binding')
router.register('template', TemplateViewset, basename='template')

urlpatterns = [
    url('', include(router.urls)),


]