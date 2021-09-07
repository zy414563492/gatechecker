<template>
  <v-app-bar
    app
    color="primary"
    dark
    clipped-left
  >

    <v-app-bar-nav-icon></v-app-bar-nav-icon>

    <v-toolbar-title>Top Bar</v-toolbar-title>

    <v-spacer></v-spacer>

    <v-btn
      href="/"
      target="_blank"
      text
    >
      <span class="mr-2">Log Out</span>
      <v-icon>mdi-open-in-new</v-icon>
    </v-btn>
  </v-app-bar>
</template>