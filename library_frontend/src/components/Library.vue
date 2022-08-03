<template>

  <v-app color="primary">

    <v-card align="center" class="my-auto" heigh="200" max-width="400">

      <v-spacer class="my-15, py-15"></v-spacer>
      

      <!-- <v-conratiner  >
        <v-card  flat >
          <v-layout row wrap >
            <v-flex xs12 md6>
              <v-chip class="displayDetailsAuthor text">Author</v-chip>
              <v-chip class="displayDetailsAuthor text">Author Name</v-chip>
            </v-flex>
            <v-flex xs12 md6>
              <v-chip class="displayDetailsBookTitle text">Book title</v-chip>
            </v-flex>
            <v-flex xs12 md6>
              <v-chip class="displayDetailsSynopsis text">Synopsis</v-chip>
            </v-flex>
          </v-layout>
        </v-card>
      </v-conratiner> -->

      <v-spacer class="my-15, py-15"></v-spacer>

      <v-btn color="teal-lighten-4" class="my-auto px-3" elevation="3">
        <v-chip>Add </v-chip>
      </v-btn>
      <v-btn color="teal-lighten-4" class="my-auto px-3" elevation="3">
        <v-chip>Other Books</v-chip>
      </v-btn>
      <v-btn color="teal-darken-3" class="mx-5 px-5" elevation="3">
        <v-chip>Same Genre</v-chip>
      </v-btn>

      <v-card-actions class="mx-2 px-3">

        <v-group-button>

          <v-btn @click="allLikes = allLikes + like" color="gray" icon=mdi-thumb-up elevation="6"></v-btn>
          <v-chip class="px-4">{{ allLikes }}</v-chip>

          <v-btn left class="px-3">
            <v-icon color="error" icon @click="show = !show" text>{{ show ? 'mdi-open-in-app' : 'mdi-collapse-all' }}
            </v-icon>
          </v-btn>

        </v-group-button>

        <v-spacer class="py-3"></v-spacer>


      </v-card-actions>

      <v-chip outlined color="error" v-show="show">

        <v-list-item>
          <v-list-item-content>
            <v-list-item-title>Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure possimus corporis ex!
              Magnam hic inventore dolor quaerat maxime, at quidem nulla et iste quae. Repudiandae quasi excepturi natus
              dolore quia.</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-form>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6">
                <v-text-field v-model="title" :rules="rules" counter="100" hint="Add you comment or tags"
                  label="Reqular"></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-form>


      </v-chip>


    </v-card>

    <!-- -->

  </v-app>

</template>

<script>

export default {
  data: () => ({

    show: false,
    allLikes: 213,
    likedBtn: false,
    like: 1

  }),
}
</script>
