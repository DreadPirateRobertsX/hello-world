from rest_framework.viewsets import ModelViewSet
from .models import Projects, Todo, Categories
from .serializers import ProjectsSerializer, TodoSerializer, UserSerializer, CategorySerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Projects, Categories
from .serializers import ProjectsSerializer, CategorySerializer

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

    @action(detail=False, methods=['get'])
    def with_ideas(self, request):
        """Custom endpoint to fetch categories with associated ideas."""
        categories = Categories.objects.all()
        data = []

        for category in categories:
            related_projects = Projects.objects.filter(category=category)
            ideas = [project.title for project in related_projects]

            data.append({
                'title': category.title,
                'ideas': ideas,
                'created_at': category.created_at
            })

        return Response(data)