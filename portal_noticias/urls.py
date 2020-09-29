from django.urls import include, path
from rest_framework import routers
from portal_noticias import views
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from api import settings

router = routers.DefaultRouter()
router.register(r'api/v1/autores', views.AutorViewSet, basename="autor")
router.register(r'api/v1/noticias', views.NoticiaViewSet, basename="noticia")


urlpatterns = [
    path('openapi/', get_schema_view(
        title="Portal de Noticias",
        version=settings.VERSION,
        description="API desenvolvida para implementar um portal de noticias",
    ), name='openapi-schema'),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),
    path('api/v1/autores/', views.AutorViewList.as_view(), name="autor"),
    path('api/v1/noticias/', views.NoticiaViewList.as_view(),  name="noticia"),
    path('', include(router.urls)),
]
