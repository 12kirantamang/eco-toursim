from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
      path('activities/', views.activities, name='activities'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('submissions/', views.contact_submissions, name='submissions'),  
    # path("contact/success/", views.contact_success, name="contact_success"),

]