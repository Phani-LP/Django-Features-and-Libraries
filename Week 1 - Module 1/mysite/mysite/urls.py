from django.contrib import admin
from django.urls import include, path
#from django.views.generic import TemplateView

urlpatterns = [
    path("", include("home.urls")),  # This line ensures the home app is the default
    path("polls/", include("polls.urls")),
    path('hello/', include('hello.urls')), #This is for session and cookie
    path("admin/", admin.site.urls),
    #path('', TemplateView.as_view(template_name='home/main.html')),
]
