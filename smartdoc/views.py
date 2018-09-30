# Create your views here.

from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView
from .models import Product, Category, Document
from .forms import ProductForm, CategoryForm, DocumentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


@method_decorator(login_required, name='dispatch')
class ProductCreate(CreateView):
    model = Product
    template_name = 'smartdoc/form.html'
    form_class = ProductForm

    # Associate form.instance.user with self.request.user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'smartdoc/form.html'
    form_class = ProductForm


class CategoryList(ListView):
    model = Category


class CategoryDetail(DetailView):
    model = Category


class CategoryCreate(CreateView):
    model = Category
    template_name = 'smartdoc/form.html'
    form_class = CategoryForm

    # Associate form.instance.user with self.request.user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CategoryUpdate(UpdateView):
    model = Product
    template_name = 'smartdoc/form.html'
    form_class = CategoryForm


class DocumentList(ListView):
    model = Document


class DocumentDetail(DetailView):
    model = Document


class DocumentCreate(CreateView):
    model = Document
    template_name = 'smartdoc/form.html'
    form_class = DocumentForm

    # Associate form.instance.user with self.request.user
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.product = Product.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


class DocumentUpdate(UpdateView):
    model = Document
    template_name = 'smartdoc/form.html'
    form_class = DocumentForm


def document_search(request):
    pass
