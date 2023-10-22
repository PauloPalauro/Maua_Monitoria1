from django.urls import path
from .views import attendance, createRecord, submitAttendance, loadAttendance
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AttendanceList, AttendanceDetail

urlpatterns = [
    path('attendance/<int:code>', attendance, name='attendance'),
    path('createRecord/<int:code>', createRecord, name='createRecord'),
    path('submitAttendance/<int:code>', submitAttendance, name='submitAttendance'),
    path('loadAttendance/<int:code>', loadAttendance, name='loadAttendance'),

    # Adicionando as URLs do DRF
    path('api/attendances/', AttendanceList.as_view(), name='attendance-list'),
    path('api/attendances/<int:pk>/', AttendanceDetail.as_view(), name='attendance-detail'),
]

# Adicionando sufixos de formato para permitir requisições com extensões como .json ou .xml
urlpatterns = format_suffix_patterns(urlpatterns)

