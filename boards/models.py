from django.db import models

# Create your models here.

class Board(models.Model): # 게시글
    title = models.CharField(max_length=10)
    content = models.TextField()  
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'id : {self.id}, title : {self.title}, content : {self.content}'
        
class Comment(models.Model): # 댓글
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    # on_delete는 참조하는 객체가 삭제될 경우 설정
    # CASCADE : 같이 삭제
    # SET_NULL : NULL 값으로 변경(NOT NULL인 경우 불가능)
    # SET_DEFAULT : DEFAULT으로 변경(DEFAULT값 없으면 불가능)
    # PROTECT : 삭제 불가
    def __str__(self):
        return f'<Board({self.board_id}):Comment({self.id})-{self.content}>'
        # 12번글의 id가 1인 댓글
        # <Board(12):Comment(1)-댓글1>