<template>
  <div class="d-flex h-100">
    <div style="margin: auto;" class="h-75 w-75">
      <div class="row justify-content-center align-items-end">
        <div class="col-4 offset-4  fs-1">Todo</div>
        <button class="col-1 offset-1 h-25 border" @click="logout">Log out</button>
      </div>
      <div class="h-100 w-100">
        <div class="h-25 d-flex align-items-center justify-content-center">
          <input type="text" class="h-25 w-50" style="border-radius: 20px; border: solid 0.5px #7d86a9;" v-model="todoItem" @keyup.enter="addTodo"/>
          <button class="h-25" style="border-radius: 10px; border: solid 0.5px #7d86a9;" @click="addTodo">추가</button>
          <button class="h-25" style="border-radius: 10px; border: solid 0.5px #7d86a9;" @click="todoItem=''">지우기</button>
          <button class="h-25" style="border-radius: 10px; border: solid 0.5px #7d86a9;" @click="todoList=[]">전체삭제</button>
        </div>
        <div class="row h-75">
          <div class="d-flex flex-column align-items-center justify-content-start">
            <div class='w-50 d-flex mb-3 p-2' style='max-width: 100%; border-bottom: 0.5px solid #f78181;' v-for="(item,index) in todoList" :key="index">
              <input class='w-75' style="border-radius: 20px; border: solid 0.5px #7d86a9;" type="text" :disabled="item.disabled" v-model="item.todo" @keyup.enter="todoEdit(index)"/>
              <button @click="todoEdit(index)" style='border-radius: 10px; border: solid 0.5px #7d86a9;' >수정</button>
              <button @click="todoDelete(index)" style='border-radius: 10px; border: solid 0.5px #7d86a9;'>삭제</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import router from '@/router'

export default {
  name: 'TodoList',
  data() {
    return {
      todoItem: '',
      todoList: [],
    }
  },
  methods: {
    todoEdit(index) {
      this.todoList[index].disabled = !this.todoList[index].disabled
    },
    todoDelete(index){
      this.todoList.splice(index,1)
    },
    addTodo(){
      if(this.todoItem == ''){
        alert('할일을 작성해주세요')
      }else{
        this.todoList.push({
          'todo': this.todoItem,
          'disabled': true
        })
      }
      this.todoItem = ''
    },
    logout(){
      localStorage.removeItem('access_token')
      router.push('/')
    }
  },
}
</script>
