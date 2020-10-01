from django.urls import path
from apiRest.api import DataApi

urlpatterns = [
    path('caso1/<int:inicio>/<int:final>/<int:paso>', DataApi.as_view(), name="apiRest"),
]
