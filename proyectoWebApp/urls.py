from django.urls import path
from proyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="Inicio"),
    path('blog', views.blog, name="Blog"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para que se pueda ver las imagenes en el navegador