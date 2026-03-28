from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static  # Fotos
import sys
from livros import views
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.admin_login, name='login'),  # Sua página login
    path('livro/<int:pk>/devolver/',
         views.marcar_devolvido, name='marcar_devolvido'),
]

# Servir arquivos de mídia em desenvolvimento (runserver)
if settings.DEBUG or any('runserver' in a for a in sys.argv):
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# Fallback explícito para servir mídia em development (garante /media/ funcionando)
if any('runserver' in a for a in sys.argv):
    urlpatterns += [
        path('media/<path:path>', serve,
             {'document_root': settings.MEDIA_ROOT}),
    ]
