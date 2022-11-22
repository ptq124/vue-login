import axios from 'axios'

function createInstance() {
  return axios.create({ baseURL: 'http://0.0.0.0:8000' })
}

function setInterceptors() {
  instance.interceptors.request.use(
    function (config) {
      const access_token = localStorage.getItem('access_token')
      config.headers.Authorization = `Bearer ${access_token}`
      return config
    },
    function (error) {
      return Promise.reject(error)
    }
  )
  instance.interceptors.response.use(
    function (response) {
      return response
    },
    function (error) {
      return Promise.reject(error)
    }
  )
  return instance
}

export const instance = createInstance()
export const http = setInterceptors()
