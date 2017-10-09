from django.shortcuts import render

# Create your views here.

def index(request):
    #create a context dictionary
    context_dict ={'text':'Hello world','number':100}
    return render(request,'index.html',context=context_dict)

def other(request):
    return render(request,'other.html')

def relative(request):
    return render(request,'relative_url_templates.html')