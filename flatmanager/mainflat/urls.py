from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
        path('', views.index, name='home'),
        path('about', views.about, name='about'),
        path('hellp', views.hellp, name='hellp'),
        path('create', views.create, name='create'),
        path("login_user", views.login_user, name="login_user"),
        path("register_user", views.register_user, name="register_user"),
        path("logout_user", views.logout_user, name="logout_user"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


