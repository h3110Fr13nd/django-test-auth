from django.urls import path

from . import views

urlpatterns = [
    path("services/", views.ServiceList.as_view()),
    path("services/<int:pk>/", views.ServiceDetail.as_view()),
    path("user/", views.get_user, name="get_user")
]


