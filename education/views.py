from django.shortcuts import render
from rest_framework import viewsets, generics

from education.models import Course, Lesson
from education.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class =CourseSerializer
    queryset = Course.objects.all()

class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIViewAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset=Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset=Lesson.objects.all()



# ListAPIView
# RetrieveAPIView
# CreateAPIView
# UpdateAPIView
# DestroyAPIView
