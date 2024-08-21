from django.urls import path
from user.views import RegistrationView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration')
]