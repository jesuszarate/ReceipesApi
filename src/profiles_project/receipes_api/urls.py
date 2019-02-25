from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('receipes', views.ReceipesViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'^receipe/', views.ReceipeApiView.as_view()),
    url(r'^ingredient/', views.IngredientApiView.as_view()),
    url(r'^ingredient/<int:pk>', views.IngredientApiView.as_view()),
    url(r'', include(router.urls))
]
