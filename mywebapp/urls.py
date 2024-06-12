from django.urls import path
from django.views.generic import TemplateView
from .views import aboutview, projectview
app_name='mywebapp'

urlpatterns = [
    path('', TemplateView.as_view(template_name='mywebapp/index.html'), name="index"),
    path('about/', aboutview, name='aboutpage' ),
    path('project/', projectview, name="project"), 

]