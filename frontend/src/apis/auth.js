import { instance } from '@/apis/index'

async function login(userData) {
  return await instance.post('/token', userData)
}

export { login }
