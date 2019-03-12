# 190311 workshop

- 앱 이름 : students

- 모델 이름 : Student
  - 모델의 필드
    - name(이름) : CharField
    - email(이메일) : CharField
    - birthday(생년월일) : DateField
    - age(나이) : IntegerField

- 학생들의 정보를 저장하는 CRUD 페이지를 구현하기 위해 아래와 같은 기능들을 추가하였다.
  - index (학생들의 이름만 나열하고, detail과 delete를 선택할 수 있음)
  - new (create 역할을 포함)
  - detail ( 학생의 상세 정보를 보기 위함)
  - delete ( 학생의 정보를 삭제하고 index로 redirect함)



