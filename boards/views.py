from django.shortcuts import render, redirect
from .models import Board
# Create your views here.

def index(request):
    boards=Board.objects.all()
    # boards=Board.objects.order_by('-id') # 이것은 최근것을 가장 위로 오게 함.
    return render(request, 'boards/index.html', {'boards':boards})
    
def new(request):
    return render(request, 'boards/new.html')

def create(request):
    board=Board()
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect('/boards/')
    
def detail(request, pk):
    board=Board.objects.get(pk=pk)
    return render(request, 'boards/detail.html', {'board':board})
    
def edit(request, pk):
    board=Board.objects.get(pk=pk)
    return render(request, 'boards/edit.html', {'board':board})
    
def update(request, pk):
    board=Board.objects.get(pk=pk)

    board.title = request.GET.get('title')
    board.content = request.GET.get('content')
    board.save()
    return redirect('/boards/')
    
def delete(request, pk):
    board=Board.objects.get(pk=pk)
    board.delete()
    return redirect('/boards/')
    

