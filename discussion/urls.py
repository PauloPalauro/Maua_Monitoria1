from django.urls import path
from .views import discussion, send, send_fac
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    StudentDiscussionList, StudentDiscussionDetail,
    FacultyDiscussionList, FacultyDiscussionDetail
)

urlpatterns = [
    path('discussion/<int:code>', discussion, name='discussion'),
    path('send/<int:code>/<int:std_id>', send, name='send'),
    path('message/<int:code>/<int:fac_id>', send_fac, name='send_fac'),

    # Adicionando as URLs do DRF
    path('api/student-discussions/', StudentDiscussionList.as_view(), name='studentdiscussion-list'),
    path('api/student-discussions/<int:pk>/', StudentDiscussionDetail.as_view(), name='studentdiscussion-detail'),
    path('api/faculty-discussions/', FacultyDiscussionList.as_view(), name='facultydiscussion-list'),
    path('api/faculty-discussions/<int:pk>/', FacultyDiscussionDetail.as_view(), name='facultydiscussion-detail'),
]

# Adicionando sufixos de formato para permitir requisições com extensões como .json ou .xml
urlpatterns = format_suffix_patterns(urlpatterns)
