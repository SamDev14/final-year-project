<template>
  <v-app>
    <v-main>
      <Navbar/>
      <Home/>
      <Search/>
      <Footer/>
      <Generate/>
    </v-main>
  </v-app>
</template>

<script>
import Navbar from './components/Navbar';
import Home from './views/home';
import Search from './views/Search';
import Footer from './components/Footer';
import Generate from './views/Generate';
//import json from './enterprise-attack.json';

export default {
  name: 'App',

  components: {
    Navbar,
    Home,
    Search,
    Footer,
    Generate,
  },

  data: () => ({
    
  }),
};
</script>
<style>
  /* #app {
  background: url('./assets/background.jpg') no-repeat center center fixed !important;
  background-size: cover;
  } */
</style>