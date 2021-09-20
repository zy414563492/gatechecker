<template>
  <v-app>
    <div>
      <v-app-bar
        app
        color="primary"
        dark
        clipped-left
      >

        <v-app-bar-nav-icon @click="drawer=!drawer; permanent=!permanent" />

        <v-toolbar-title>Demo App</v-toolbar-title>

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
    </div>

    
    <v-navigation-drawer
      v-model="drawer"
      :permanent="permanent_by_size"
      app
      clipped
      :absolute="absolute_by_size"
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            For Manager
          </v-list-item-title>
          <v-list-item-subtitle>
            V1.0
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :to="item.link"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            For Client
          </v-list-item-title>
          <v-list-item-subtitle>
            V1.0
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items_client"
          :key="item.title"
          :to="item.link"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

    </v-navigation-drawer>


    <v-main>
      <router-view/>
    </v-main>

  </v-app>
</template>

<script>
export default {
  name: 'App',

  data: () => ({
    drawer: true,
    permanent: true,
    items: [
      { title: 'ダッシュボード', icon: 'mdi-view-dashboard', link: '/' },
      { title: 'エンドユーザー', icon: 'mdi-account-multiple', link: '/endusers' },
      { title: '施設', icon: 'mdi-office-building-marker', link: '/buildings' },
      { title: 'ゲート', icon: 'mdi-door', link: '/gates' },
      { title: 'デバイス', icon: 'mdi-devices', link: '/devices' },
      { title: '検温記録', icon: 'mdi-checkbook', link: '/logs' },
      { title: '全体確認', icon: 'mdi-eye-outline', link: '/status' },
    ],
    items_client: [
      // { title: 'ログイン', icon: 'mdi-login-variant', link: '/login' },
      { title: '現場確認', icon: 'mdi-eye-outline', link: '/login' },
    ],
    right: null,
  }),

  computed: {
    permanent_by_size () {
      switch (this.$vuetify.breakpoint.name) {
        case 'xs': return false
        case 'sm': return false
        case 'md': return this.permanent
        case 'lg': return this.permanent
        case 'xl': return this.permanent
      }
    },

    absolute_by_size () {
      switch (this.$vuetify.breakpoint.name) {
        case 'xs': return false
        case 'sm': return false
        case 'md': return true
        case 'lg': return true
        case 'xl': return true
      }
    },
  },

};
</script>
