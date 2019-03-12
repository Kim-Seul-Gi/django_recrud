import pprint
from django.shortcuts import render, redirect
from .models import Board, Comment

# Create your views here.

def index(request):
    # print()
    # pprint.pprint(request.META)
    # print()
    # pprint.pprint(type(request))
    # print()
    # pprint.pprint(dir(request))
    boards=Board.objects.all()
    
    # boards=Board.objects.order_by('-id') # 이것은 최근것을 가장 위로 오게 함.
    return render(request, 'boards/index.html', {'boards':boards})
    
def new(request):
    if request.method == 'POST': # 직접 인풋을 실행한 경우(create 역할)
        board=Board()
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk) # redirect('/boards/') 와 같은 의미이다. 왜냐하면 boards/urls.py 에서 name으로 정의했으므로
    else: # get 형식으로 햇으면 아무것도 하지않는다.(기존의 new 역할)
        return render(request, 'boards/new.html')
        
# def create(request): # 이것을 주석처리 할 때에는 앱/urls.py 에서 해당 함수를 주석처리 해야 한다.
#     board=Board()
#     board.title = request.POST.get('title')
#     board.content = request.POST.get('content')
#     board.save()
#     return redirect('boards:detail', board.pk) # redirect('/boards/') 와 같은 의미이다. 왜냐하면 boards/urls.py 에서 name으로 정의했으므로
     
def detail(request, board_pk):
    board=Board.objects.get(pk=board_pk)
    comments = board.comment_set.all()

    # 다수의 comments를 가져오기 위해서 board 아이디에 해당하는 모든 comment들을 가져옴.
    return render(request, 'boards/detail.html', {'board':board, 'comments':comments})
    
def edit(request, board_pk):
    if request.method == 'POST': # 기존의 update 역할
        board=Board.objects.get(pk=board_pk)
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else:    # 기존의 edit 역할, get 형식은 url로 주고받고 하는 형식?? 이므로 ㅇㅇ
        board=Board.objects.get(pk=board_pk)
    return render(request, 'boards/edit.html', {'board':board})
    
# def update(request, pk):  # 이것을 주석처리 할 때에는 앱/urls.py 에서 해당 함수를 주석처리 해야 한다.
#     board=Board.objects.get(pk=pk)
#     board.title = request.GET.get('title')
#     board.content = request.GET.get('content')
#     board.save()
#     return redirect('boards:detail', board.pk)
    
def delete(request, board_pk):
    if request.method == 'POST': # 직접 html에서 제출을 눌렀을 경우 - POST 형식
        board=Board.objects.get(pk=board_pk)
        board.delete()
        return redirect('boards:index')
    else: # 제출을 누른것이 아니라 url 자체를 실행한 경우>GET 형식이다., ex) boards/1/delete/ 를 실행
        board=Board.objects.get(pk=board_pk) # 하면 실행 안되게함ㅎㅎ 
        return redirect('boards:detail', board.pk)
        
def comments_create(request, board_pk):
    # 1. 댓글 달 게시물을 가져온다.
    board = Board.objects.get(pk=board_pk)
    # 2. 댓글을 저장한다
    comment = Comment()
    comment.content = request.POST.get('content')
    comment.board = board
    comment.save()
    return redirect('boards:detail', comment.board_id)
    
def comments_delete(request, board_pk, comment_pk):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
    
    return redirect('boards:detail', board_pk)
    
