<template>
  <v-breadcrumbs :items="items">
    <template v-slot:divider>
      <v-icon>mdi-chevron-right</v-icon>
    </template>
  </v-breadcrumbs>
</template>

<script>
  export default {
    props: ['subLink'],
    data () {
      return {
        items: [
          {
            text: 'Home',
            disabled: false,
            href: '/',
          },
          {
            text: this.subLink,
            disabled: true,
          },
        ],
      }
    },
  }
</script>
