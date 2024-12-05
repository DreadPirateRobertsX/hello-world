from .views import ProjectsViewSet, TodoViewSet, UserViewSet, CategoryViewSet
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'todos', TodoViewSet)
router.register(r'projects', ProjectsViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls
