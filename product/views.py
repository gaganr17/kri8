from django.shortcuts import render

# Create your views here.
def product(req):
    return render(req, "product/product.html")
