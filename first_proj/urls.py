"""first_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from rest_framework import routers
from first_app import views 
from first_app.views import ProblemSolutionView

router = routers.DefaultRouter()
router.register(r'contest',views.ContestViewSet)
router.register(r'challenge',views.ChallengeViewSet)
router.register(r'college',views.CollegeViewSet)

router.register(r'total_view',views.TotalViewSet)

router.register(r'total_submission',views.SubmissionViewSet)

#router.register(r'api/problemsolution',views.ProblemSolutionView,'api')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include(router.urls)),
    url(r'^api/problemsolution/$',ProblemSolutionView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
