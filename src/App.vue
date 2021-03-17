<template>
  <v-app>
    <v-main>
      <Navbar/>
      <home />
      <Search/>
      <Footer/>
      <Generate/>
    </v-main>
  </v-app>
</template>

<script>
import Navbar from './components/Navbar';
import home from './views/home';
import Search from './views/Search';
import Footer from './components/Footer';
import Generate from './views/Generate';

export default {
  name: 'App',

  components: {
    Navbar,
    home,
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