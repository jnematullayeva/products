from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import *
from .models import *

class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'products/create.html', context={'form': form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')
        return render(request, 'products/create.html', context={'form': form})

class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'products/list.html', context={'products': products})


class ProductUpdateView(View):
    def get(self, request,pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'products/update.html', context = {'form': form, 'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk = pk)
        form = ProductForm(request.Post, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')
        return render(request, 'products/update.html', context={'form': form, 'product': product})

class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'products/detail.html', context={'product': product})

class ProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'products/delete.html', context={'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('product-list')
        
