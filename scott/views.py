from django.views import generic
from .models import Dept


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'watchlist/index.html'
    context_object_name = 'latest_dept_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Dept.objects.all()
