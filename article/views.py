from datetime import datetime

from django.views import generic
from django.views.generic import ListView, DetailView

from .models import Article, Category


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'article/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.filter(date_time__lte=datetime.now()).order_by('-date_time')[:5]


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category
