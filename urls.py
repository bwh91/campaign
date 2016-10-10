from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'(?P<slug>[-\w]*)/',
        views.CampaignView.as_view(),
        name='campaign_view'
        ),
]
