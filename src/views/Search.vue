<template>
  <v-card>
    <v-tabs 
      v-model="tab"
      background-color="primary"
      dark
    >
      <v-tab 
        v-for="item in items" 
        :key="item.name"
      >
      {{item.tab}}
      </v-tab>
    </v-tabs>

    <v-tab-items v-model="tab">
      <v-tab-item 
        v-for="item in items"
        :key="item.tab"
      >
        <v-card flat>
          <v-card-text>{{item.content}}</v-card-text>
        </v-card>
      </v-tab-item>
    </v-tab-items>
  </v-card>
</template>

<script>
export default {
  name: 'home',

  components: {
    
  },

  data: () => ({
    tab: null,
    items: [
      { tab: 'Deceptive Interactions', 
        content: '#'},
      { tab: 'Abuse Existing Functionality', 
        content: '#'},
      { tab: 'Manipulate Data Structures', 
        content: '#'},
      { tab: 'Manipulate System Resources', 
        content: '#'},
      { tab: 'Code Injection', 
        content: '#'},
      { tab: 'Employ Probabalistic Techniques', 
        content: '#'},
      { tab: 'Manipulate Timing and State', 
        content: '#'},
      { tab: 'Collect and Analyze Information', 
        content: '#'},
      { tab: 'Subvert Access Control', 
        content: '#'}
    ],
    checked: [],
  }),

  methods: {
    contentAdd(checked) {
      for (i=0; i <= checked.length; i++) {
        
      }
    }

    contentChecked() {
      if items.content ==  {
        //items.content.push(checked)
      }
    }
  }
};
</script>