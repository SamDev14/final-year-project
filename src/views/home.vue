<template>
  <v-card>
    <v-banner dense fixed class="banner pa-4">
        <p></p>
        <h1>{{banner_heading}}</h1>
        <p></p>
        <p>{{banner_text}}</p>
    </v-banner>
  </v-card>
</template>

<script>
export default {
  name: 'Home',

  components: {
    
  },

  data: () => ({
    banner_heading: "Welcome To My Final Year Project",
    banner_text: "A tool for assisting Blue Teamers in threat mitigation and response.",
  }),
};
</script>
<style>
  
</style>