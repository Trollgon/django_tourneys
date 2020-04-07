<template>
  <div id="app">
    <nav class="navbar navbar-light bg-light">
      <a class="navbar-brand" href="#">Home</a>
      <form class="form-inline">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">
          <font-awesome-icon icon="sign-in-alt" /> Login
        </button>
      </form>
    </nav>
    <router-view/>
  </div>
</template>

<script>
  export default {
    name: 'App'
  }
</script>
