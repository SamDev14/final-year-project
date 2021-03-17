<template>
    <v-app-bar color="primary" absolute
      dark>
      <h1>UP877426</h1>
      <v-btn color="primary" elevation="0"  v-for="link in links" :key="link">{{link}}</v-btn>
    </v-app-bar>

</template>

<script>
export default {
  name: 'App',

  components: {

  },

  data: () => ({
    links: ["Home","Documentation","FAQ","Contact"],
  }),
};
</script>