from django.urls import path
from .views import FraudPredictionView

urlpatterns = [
    path('predict/', FraudPredictionView.as_view(), name='fraud-prediction'),
]
