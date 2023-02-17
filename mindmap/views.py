import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from mindmap.models import Node
# Create your views here.
global is_add_node
is_add_node = [False, ""]


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
    n = Node(text=is_add_node[1], x=body["mousex"], y=body["mousey"])
    n.save()
    if request.method == 'POST':
        response = redirect("/mindmap/")
         # HTTP 1.1.
        is_add_node = [False,""]
        return response 
