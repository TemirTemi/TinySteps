"""TinySteps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from tutors.views import MainView, AboutView, GoalsView, BookingView, BookingDoneView

urlpatterns = [
    path('teachers/', MainView.as_view()),
    path('profile/<int:teacher_id>', AboutView.as_view()),
    path('teachers/<str:teacher_goals>', GoalsView.as_view()),
    path('booking/<int:teacher_id>/<str:teacher_free_time>', BookingView.as_view()),
    path('booking_done/<str:time>/<str:name>,<str:number>', BookingDoneView.as_view()),
]
