from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views
from froala_editor import views as froala_views


admin.site.site_header = "Mauá Monitoria"
admin.site.site_title = "Mauá Monitoria Portal de Administração"
admin.site.index_title = "Bem vindo ao  Portal de Administração do Mauá Monitoria "


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('student/', views.guestStudent, name='guestStudent'),
    path('teacher/', views.guestFaculty, name='guestFaculty'),
    path('', include('main.urls')),
    path('', include('discussion.urls')),
    path('', include('attendance.urls')),
    path('', include('quiz.urls')),
    path('froala_editor/', include('froala_editor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
