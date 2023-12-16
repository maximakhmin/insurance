from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('index', views.getIndex),                           # permit all
    path('auto', views.getAuto),                             # permit all
    path('accident', views.getAccident),                     # permit all
    path('property', views.getPropetry),                     # permit all
    path('auto/<int:id>/calculate', views.calculateAuto),    # permit authenticated
    path('auto/<int:id>/buy', views.buyAuto),                # permit authenticated
    path('accident/<int:id>/buy', views.buyAccident),        # permit authenticated
    path('property/<int:id>/buy', views.buyPropetry),        # permit authenticated
    path('policies', views.getPolicies),                     # permit authenticated
]