from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='home'),
        path('about', views.about, name='about'),
        path('hellp', views.hellp, name='hellp'),
        path('create', views.create, name='create')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
