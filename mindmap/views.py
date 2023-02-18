import json
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from mindmap.models import Node,Relation
# Create your views here.
global is_add_node
is_add_node = [False, ""]
global relation
relation = []

def index(request):
    global is_add_node

    template_name = 'mindmap/index.html'
    lines = []
    nodes = list(Node.objects.all().values())
    rela = Relation.objects.all().values()
    rela = list(rela.values())
    print(rela)
    for this_rela in rela:
        node1 = Node.objects.get(pk=this_rela['node1']).__dict__
        node2 = Node.objects.get(pk=this_rela['node2']).__dict__
        line = {"x1":node1["x"]+60 ,"y1":node1["y"]-50 , "x2":node2["x"]+60,"y2":node2["y"]-50}
        lines.append(line)
    context = {'nodes': nodes, 'addnode_url': "mindmap/addnode",
               "is_add_node": is_add_node[0],"lines":lines}
    
    return HttpResponse(render(request, template_name, context))


def addnode(request):
    global is_add_node
    is_add_node = [True, request.POST.get('text')]
    return redirect("/mindmap/")


@csrf_exempt
def addnode_put(request):
    global is_add_node
    body = json.loads(request.body)
    n = Node(text=is_add_node[1], x=body["mousex"], y=body["mousey"]-50)
    n.save()
    if request.method == 'POST':
        response = redirect("/mindmap/")
         # HTTP 1.1.
        is_add_node = [False,""]
        return response 

@csrf_exempt
def add_relation(request):
    global relation
    body = json.loads(request.body)
    relation.append(body["id"])
    while(len(relation) >=2): 
        node1 = relation.pop()
        node2 = relation.pop()
        node1,node2 = (min(node1,node2) , max(node1,node2))
        
        r = Relation(node1=node1,node2=node2)
        r.save()
        
    return redirect("/mindmap/")

@csrf_exempt
def reset_db(request):
    Node.objects.all().delete()
    Relation.objects.all().delete()
    return redirect("/mindmap/")