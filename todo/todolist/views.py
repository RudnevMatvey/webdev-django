from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect

# Create your views here.
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todolist.html', {'all_items': all_todo_items})
def addTodoView(request):
    x = request.POST['content']
    new_item = TodoItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todolist')
