from django.urls import URLPattern, path
from .views import CampaignListAPIView

urlpatterns = [
    path('campaigns/', CampaignListAPIView.as_view(), name="campaigns")
]
