from django.shortcuts import render

# Create your views here.
def index(req):
    # dct = {"insert": "Hi"}
    return render(req, "index/index.html")
