from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from vote.models import VoteTopic


class FirstView(TemplateView):
    template_name = "base.html"

class SecondView(ListView):
    template_name = "vote/topic_list.html"
    queryset = VoteTopic.objects.all()