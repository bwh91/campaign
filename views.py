from django.shortcuts import render
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from . models import Campaign

# Create your views here.

class CampaignView(DetailView):
    model = Campaign

    def get_object(self):
        return get_object_or_404(Campaign, slug=self.kwargs.get("slug"))

    #def get_context_data(self, **kwargs):
        #context = super(CampaignView, self).get_context_data(**kwargs)
        #context['header'] =
        #context['footer'] =
        #return context
