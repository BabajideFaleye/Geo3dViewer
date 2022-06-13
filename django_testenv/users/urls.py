from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='register'),
    path('UserAccountCreated', views.userAccountCreated, name='UserAccountCreated')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)