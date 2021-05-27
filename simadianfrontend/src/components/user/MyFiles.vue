<template>
  <v-card
    class="mx-auto"
    max-width="1000"
    style="margin-top: 20px"
  >
    <v-toolbar
      color="pink"
      dark
    >

      <v-toolbar-title>Sent</v-toolbar-title>

      <v-spacer></v-spacer>

    </v-toolbar>

    <v-list two-line>
      <v-list-item-group
        v-model="selected"
        active-class="pink--text"
        multiple
      >
        <template v-for="(item, index) in items">
          <v-list-item :key="item.title" @click="goTo">
            <template v-slot:default="{ active }">
              <v-list-item-content>

                <v-list-item-subtitle v-text="item.data"></v-list-item-subtitle>

              </v-list-item-content>
            </template>
          </v-list-item>

          <v-divider
            v-if="index < items.length - 1"
            :key="index"
          ></v-divider>
        </template>
      </v-list-item-group>
    </v-list>
  </v-card>
</template>

<script>
  export default {
    data: () => ({
      selected: [2],
      items: [
        {
          action: '15 min',
          headline: 'Brunch this weekend?',
          data: `I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
          title: 'Ali Connors',
        },
        {
          action: '2 hr',
          headline: 'Summer BBQ',
          data: `Wish I could come, but I'm out of town this weekend.`,
          title: 'me, Scrott, Jennifer',
        },
        {
          action: '6 hr',
          headline: 'Oui oui',
          data: 'Do you have Paris recommendations? Have you ever been?',
          title: 'Sandra Adams',
        },
        {
          action: '12 hr',
          headline: 'Birthday gift',
          data: 'Have any ideas about what we should get Heidi for her birthday?',
          title: 'Trevor Hansen',
        },
        {
          action: '18hr',
          headline: 'Recipe to try',
          data: 'We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
          title: 'Britta Holt',
        },
      ],
    }),

    methods: {
        goTo() {
            window.location.href = "https://www.geeksforgeeks.org/";
        }
    }
  }
</script>