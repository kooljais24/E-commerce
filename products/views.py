from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.

from .models import Product
class ProductListView(ListView):
	queryset=Product.objects.all()
	template_name="products/list.html"

class ProductDetailView(DetailView):
	queryset=Product.objects.all()
	template_name="products/detail.html"