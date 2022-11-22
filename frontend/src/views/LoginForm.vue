<template>
  <div class="d-flex h-100">
    <div style="margin: auto" class="h-50 w-50">
      <div class="row h-25 align-items-end">
        <div class="text-center fs-1">login</div>
      </div>
      <div
        class="row h-50 flex-column align-items-center justify-content-center"
      >
        <div class="w-50">
          <input
            type="text"
            class="form-control"
            placeholder="Username"
            style="
              border-radius: 25px;
              border: solid 0.5px #7d86a9;
              padding: 12px 10px;
            "
            v-model="username"
            @keyup.enter="login()"
          />
        </div>
        <div class="w-50 mt-3">
          <input
            type="password"
            class="form-control"
            placeholder="Password"
            style="
              border-radius: 25px;
              border: solid 0.5px #7d86a9;
              padding: 12px 10px;
            "
            v-model="password"
            @keyup.enter="login()"
          />
        </div>
      </div>
      <div class="row h-25 justify-content-center">
        <div class="w-50">
          <button
            type="button"
            class="btn btn-outline-secondary w-100"
            style="padding: 12px 10px; border-radius: 25px"
            @click="login"
          >
            Login
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { login } from '@/apis/auth'
export default {
  name: 'LoginForm',
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    async login() {
      try {
        const params = new URLSearchParams()
        params.append('username', this.username)
        params.append('password', this.password)
        const res = await login(params)
        localStorage.setItem('access_token', res.data.access_token)
        this.$router.push('/todo')
      } catch (e) {
        alert('로그인 오류')
      }
    },
  },
}
</script>
