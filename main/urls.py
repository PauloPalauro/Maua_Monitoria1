from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    StudentList, StudentDetail, FacultyList, FacultyDetail, DepartmentList, DepartmentDetail,
    CourseList, CourseDetail, AnnouncementList, AnnouncementDetail, AssignmentList, AssignmentDetail,
    SubmissionList, SubmissionDetail, MaterialList, MaterialDetail
)

urlpatterns = [
    path('', views.std_login, name='std_login'),
    path('my/', views.myCourses, name='myCourses'),
    path('facultyCourses/', views.facultyCourses, name='facultyCourses'),
    path('login/', views.std_login, name='std_login'),
    path('logout/', views.std_logout, name='std_logout'),
    path('my/<int:code>/', views.course_page, name='course'),
    path('profile/<str:id>/', views.profile, name='profile'),
    path('facultyProfile/<str:id>/', views.profile, name='profile_faculty'),
    path('faculty/<int:code>/', views.course_page_faculty, name='faculty'),
    path('addAnnouncement/<int:code>/', views.addAnnouncement, name='addAnnouncement'),
    path('announcement/<int:code>/<int:id>/', views.deleteAnnouncement, name='deleteAnnouncement'),
    path('edit/<int:code>/<int:id>/', views.editAnnouncement, name='editAnnouncement'),
    path('update/<int:code>/<int:id>/', views.updateAnnouncement, name='updateAnnouncement'),
    path('addAssignment/<int:code>/', views.addAssignment, name='addAssignment'),
    path('assignment/<int:code>/<int:id>/', views.assignmentPage, name='assignmentPage'),
    path('assignments/<int:code>/', views.allAssignments, name='allAssignments'),
    path('student-assignments/<int:code>/', views.allAssignmentsSTD, name='student-assignments'),
    path('addSubmission/<int:code>/<int:id>/', views.addSubmission, name='addSubmission'),
    path('submission/<int:code>/<int:id>/', views.viewSubmission, name='submission'),
    path('gradeSubmission/<int:code>/<int:id>/<int:sub_id>', views.gradeSubmission, name='gradeSubmission'),
    path('course-material/<int:code>/', views.addCourseMaterial, name='addCourseMaterial'),
    path('course-material/<int:code>/<int:id>/', views.deleteCourseMaterial, name='deleteCourseMaterial'),
    path('courses/', views.courses, name='courses'),
    path('departments/', views.departments, name='departments'),
    path('access/<int:code>/', views.access, name='access'),
    path('changePasswordPrompt/', views.changePasswordPrompt, name='changePasswordPrompt'),
    path('changePhotoPrompt/', views.changePhotoPrompt, name='changePhotoPrompt'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('changePasswordFaculty/', views.changePasswordFaculty, name='changePasswordFaculty'),
    path('changePhoto/', views.changePhoto, name='changePhoto'),
    path('changePhotoFaculty/', views.changePhotoFaculty, name='changePhotoFaculty'),
    path('search/', views.search, name='search'),
    path('error/', views.error, name='error'),

    # Adicionando as URLs do DRF
    path('api/students/', StudentList.as_view(), name='student-list'),
    path('api/students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
    path('api/faculties/', FacultyList.as_view(), name='faculty-list'),
    path('api/faculties/<int:pk>/', FacultyDetail.as_view(), name='faculty-detail'),
    path('api/departments/', DepartmentList.as_view(), name='department-list'),
    path('api/departments/<int:pk>/', DepartmentDetail.as_view(), name='department-detail'),
    path('api/courses/', CourseList.as_view(), name='course-list'),
    path('api/courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('api/announcements/', AnnouncementList.as_view(), name='announcement-list'),
    path('api/announcements/<int:pk>/', AnnouncementDetail.as_view(), name='announcement-detail'),
    path('api/assignments/', AssignmentList.as_view(), name='assignment-list'),
    path('api/assignments/<int:pk>/', AssignmentDetail.as_view(), name='assignment-detail'),
    path('api/submissions/', SubmissionList.as_view(), name='submission-list'),
    path('api/submissions/<int:pk>/', SubmissionDetail.as_view(), name='submission-detail'),
    path('api/materials/', MaterialList.as_view(), name='material-list'),
    path('api/materials/<int:pk>/', MaterialDetail.as_view(), name='material-detail'),
]

# Adicionando sufixos de formato para permitir requisições com extensões como .json ou .xml
urlpatterns = format_suffix_patterns(urlpatterns)
