<template>
  <v-navigation-drawer app permanent clipped>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="text-h6">
          Demo APP
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
  </v-navigation-drawer>
</template>

<script>
  export default {
    data () {
      return {
        items: [
          { title: 'ダッシュボード', icon: 'mdi-view-dashboard', link: '/' },
          { title: 'エンドユーザー', icon: 'mdi-account-multiple', link: '/endusers' },
          { title: '施設', icon: 'mdi-office-building-marker', link: '/buildings' },
          { title: 'ゲート', icon: 'mdi-door', link: '/gates' },
          { title: 'デバイス', icon: 'mdi-devices', link: '/devices' },
          { title: '検温記録', icon: 'mdi-checkbook', link: '/logs' },
        ],
        right: null,
      }
    },
  }
</script>
