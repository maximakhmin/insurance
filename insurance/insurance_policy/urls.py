from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('policy', views.PolicyView().as_view()),                # permit staff
    path('policy/<int:id>', views.PolicyViewOne().as_view()),    # permit staff
    path('policy/<int:id>/activate', views.activatePolicy),      # permit staff
    path('policy/<int:id>/deactivate', views.deactivatePolicy),  # permit staff
]