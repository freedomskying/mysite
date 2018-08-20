from django.shortcuts import render

from django.views import generic
from .models import Article
from datetime import timezone


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'article/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.filter(date_time__lte=timezone.now()).order_by('-date_time')[:5]
