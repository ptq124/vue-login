# 구현기능

backend(간단하게)

fastapi로 token api를 만들어 username과 password를 받으면 access_token을 반환하도록 구현

frontend

vue Login, TodoList

- login 기능 구현 token api를 call하여 로컬스토리지에 저장 
- todolist 추가, 지우기, 전체삭제, 수정, 개별삭제 기능 구현
- logout 기능 구현 (네비게이션 가드(로컬스토리지를 검사하여 토큰이 없을경우 로그인 페이지로, 로컬스토리지 토큰 삭제)
- ID,PASSWORD validation 기능 
