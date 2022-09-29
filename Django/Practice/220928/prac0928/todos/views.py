from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all().order_by('completed', 'priority')
    
    context = {
        "todos" : todos,
    }
    return render(request, 'todos/index.html', context)

def create(request):
    # get을 이용
    content = request.GET.get("content_")
    priority = request.GET.get("priority_")
    deadline = request.GET.get("deadline_")
    
    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    return redirect('todos:index')

def delete(request, todo_pk):
    # 함수의 인자, get 뒤에 쓰는 인자, urls의 app 뒤에 붙이는 동적인자 이 셋이
    # 일치해야함!
    todo = Todo.objects.get(pk = todo_pk)
    todo.delete()

    return redirect('todos:index')

def update(request, todo_pk):
     # update할 특정 데이터를 불러온다. -> pk 를 사용해서
    todo = Todo.objects.get(pk = todo_pk)

    # 버튼 눌렀을 때 False였다면 True로 바꿔주면서 전부 가로줄 그어주기
    if todo.completed == False:
        todo.completed = True
    else:
        todo.completed = False

    # 데이터를 수정한 것을 반영(save)
    todo.save()

    # 데이터의 디테일 페이지로 리다이렉트
    return redirect('todos:index')
    
