from django.urls import path,include
from .views import *
from blog import views as  blog_vw
from gallery import views as gallery_vw
from rest_framework import routers

router = routers.DefaultRouter()
router.register('partners',PartnerViewsets )
router.register('articls',blog_vw.ArticleViewsets )
router.register('cases',gallery_vw.CaseViewsets)
router.register('programs',gallery_vw.ProgramViewsets)
router.register('Files',gallery_vw.GalleryFileViewsets)

urlpatterns = [
    path('',home,name='home'),
    path('api-auth/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]