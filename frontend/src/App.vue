<template>
  <div id="app">
    <main class="container h-100">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>
<style>
body {
  margin: 0;
  height: 100vh;
}
#app {
  background-color: #f5f6ce;
  height: 100%;
}
</style>
