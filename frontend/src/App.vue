<template>
  <v-app>

    <v-app-bar flat app color="gray darken" dark>

      <div class="d-flex align-center">
        <v-img elevation="5" alt="Library Logo" class="shrink mr-2" contain
          src="https://d2sz1kgdtrlf1n.cloudfront.net/task_images/DcRJ1638518889088-Original20Logo.png"
          transition="scale-transition" width="40" />
      </div>

      <v-spacer></v-spacer>


      <v-chip label elevation="5" class="mr-auto" color="orange darken-4">TopUp Mama Library</v-chip>
      <v-icon>mdi-books</v-icon>
    </v-app-bar>

    <v-card :loading="loading" class="mx-auto my-12" max-width="374">
      <template slot="progress">
        <v-progress-linear color="orange darken-4" height="10" indeterminate></v-progress-linear>
      </template>
    </v-card>

    <v-img height="250"
      src="https://images.unsplash.com/photo-1507842217343-583bb7270b66?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=990&q=80">
    </v-img>

    <v-card class="py-3  my-4 mx-0">
      <v-card-title class="py">
        <v-chip small label class="font-weight-light">Book : {{ book }}</v-chip>
      </v-card-title>
      <v-card-subtitle class=" py-2  text-subtitle-2 font-weight-light">
        <v-chip small label>Author : {{ author }}</v-chip>
      </v-card-subtitle>
      <v-card-subtitle elevation="4" small color="white--text" class="py-5  mx-2 text-subtitle-5 font-weight-light">
        Publisher : {{ publisher }}
      </v-card-subtitle>

      <v-row align="center" class="my-3 mx-2">

        <div class="error--text ms-4">
          <v-chip label class="px-3" elevation="2" color='orange--text' small>
            <v-icon class="mx-1" elevation="4" color='orange darken-4' small>mdi-thumb-up</v-icon>Likes
          </v-chip>
          <v-chip label class="mx-1" elevation="4" color='orange--text' small>346</v-chip>

          <v-text-field elevation="5" small class="mx-0 py-2  mx-auto" label="Add your comment ..." solo dense
            width="50">
          </v-text-field>

          <v-btn color="orange darken-4" elevation="3" small @click="snackbar = true">Add</v-btn>
          <v-snackbar v-model="snackbar">
            {{ text }}
            <template v-slot:action="{ attrs }">
              <v-btn color="pink" text v-bind="attrs" @click="snackbar = false">
                Close
              </v-btn>
            </template>
          </v-snackbar>

        </div>
      </v-row>
    </v-card>

    <v-card-title class="font-weight-bold">Library query</v-card-title>


    <v-card-text>
      <v-chip-group v-model="selection" active-class="orange darken-4 accent-5 white--text"
        transition="scale-transition" column>
        <v-chip label icon="">Authors</v-chip>

        <v-chip label>Other Books</v-chip>

        <v-chip label>Charactors</v-chip>

      </v-chip-group>
    </v-card-text>


    <v-card dense>
      <v-expansion-panels>
        <v-expansion-panel>
          <v-expansion-panel-header color="orange darken-4" class="subheading font-weight-light" text
            @click="anonymous_comments">
            {{ commentTitle }}
          </v-expansion-panel-header>
          <v-divider></v-divider>
          <v-expansion-panel-content v-for="(comments, comment) in 5" :key="comment" class="font-weight-light">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi ipsa architecto quia necessitatibus
            tenetur velit, tempore maxime voluptates deserunt. Ratione maiores iusto sint consectetur. Animi
            mollitia numquam enim in. Non.
            <v-chip label>
            <v-rating  background-color="orange darken-4" color="orange darken-4" size="15"></v-rating>
            </v-chip>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>

    </v-card>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    loading: false,
    selection: 0,
    commentTitle: "Anonymous comments",
    commentRatings: 15,
    snackbar: false,
    text: "Comment added"
  }),

  methods: {
    anonymous_comments() {
      this.loading = true

      setTimeout(() => (this.loading = false), 2000)
    },
  },
}
</script>
