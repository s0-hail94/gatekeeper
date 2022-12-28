from django.urls import path
from user.views import CreateUserView, LoginView, LogoutView



urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', CreateUserView.as_view()),
    path('logout/', LogoutView.as_view()),
]
