<template>
  <v-app>
    <v-main>
      <v-container class="mx-10">
        <Library />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Library from './components/Library.vue'

export default {
  name: 'App',

  components: {
    Library,
  },

  data () {
      return {
        title: 'Preliminary report',
        description: 'California is a state in the western United States',
        rules: [v => v.length <= 25 || 'Max 25 characters'],
        wordsRules: [v => v.trim().split(' ').length <= 5 || 'Max 5 words'],
      }
    },
}

</script>
