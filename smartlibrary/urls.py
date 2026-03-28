from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from livros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.admin_login, name='login'),
    path('livro/<int:pk>/devolver/', views.marcar_devolvido, name='marcar_devolvido'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
