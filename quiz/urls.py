from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import QuizList, QuizDetail, QuestionList, QuestionDetail, StudentAnswerList, StudentAnswerDetail

urlpatterns = [
    path('quiz/<int:code>', views.quiz, name='quiz'),
    path('addQuestion/<int:code>/<int:quiz_id>', views.addQuestion, name='addQuestion'),
    path('allQuizzes/<int:code>', views.allQuizzes, name='allQuizzes'),
    path('quizSummary/<int:code>/<int:quiz_id>', views.quizSummary, name='quizSummary'),
    path('myQuizzes/<int:code>', views.myQuizzes, name='myQuizzes'),
    path('startQuiz/<int:code>/<int:quiz_id>', views.startQuiz, name='startQuiz'),
    path('studentAnswer/<int:code>/<int:quiz_id>', views.studentAnswer, name='studentAnswer'),
    path('quizResult/<int:code>/<int:quiz_id>', views.quizResult, name='quizResult'),

    # Adicionando as URLs do DRF
    path('api/quizzes/', QuizList.as_view(), name='quiz-list'),
    path('api/quizzes/<int:pk>/', QuizDetail.as_view(), name='quiz-detail'),
    path('api/questions/', QuestionList.as_view(), name='question-list'),
    path('api/questions/<int:pk>/', QuestionDetail.as_view(), name='question-detail'),
    path('api/student-answers/', StudentAnswerList.as_view(), name='studentanswer-list'),
    path('api/student-answers/<int:pk>/', StudentAnswerDetail.as_view(), name='studentanswer-detail'),
]

# Adicionando sufixos de formato para permitir requisições com extensões como .json ou .xml
urlpatterns = format_suffix_patterns(urlpatterns)
