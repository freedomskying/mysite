from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'dmreport/index.html'
    context_object_name = ''

    def get_queryset(self):
        """Return the last five published questions."""
        return ''
