from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
def index(request):
    template = loader.get_template('mindmap/index.html')
    nodes = []
    context = {'nodes':nodes, 'addnode_url': "mindmap/addnode" }
    return HttpResponse(template.render(context,request))

def addnode(request):
    
    return HttpResponse("test")