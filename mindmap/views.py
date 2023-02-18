import json
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

    nodes = list(Node.objects.all().values())
    context = {'nodes': nodes, 'addnode_url': "mindmap/addnode",
               "is_add_node": is_add_node[0]}
    print(nodes)

    return HttpResponse(render(request, template_name, context))


def addnode(request):
    global is_add_node
    is_add_node = [True, request.POST.get('text')]
    return redirect("/mindmap/")


@csrf_exempt
def addnode_put(request):
    global is_add_node
    body = json.loads(request.body)
    n = Node(text=is_add_node[1], x=body["mousex"], y=body["mousey"]-100)
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
        print(node1,node2)
        r = Relation(node1=node1,node2=node2)
        r.save()
        print("add relation:",r,list(Relation.objects.all().values()))
    return redirect("/mindmap/")