from rest_framework import serializers
from main.models import Student, Faculty, Course
from .models import StudentDiscussion, FacultyDiscussion

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentDiscussionSerializer(serializers.ModelSerializer):
    sent_by = StudentSerializer()

    class Meta:
        model = StudentDiscussion
        fields = '__all__'

class FacultyDiscussionSerializer(serializers.ModelSerializer):
    sent_by = FacultySerializer()

    class Meta:
        model = FacultyDiscussion
        fields = '__all__'
