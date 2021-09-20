<template>
   <v-app>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>{{ name }}</v-toolbar-title>
              </v-toolbar>

              <v-card-text>
                <v-row>
                  <v-col cols="6">
                    <v-subheader>{{ "施設名：" + count_info.name }}</v-subheader>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col cols="6">
                    <v-subheader>本日の入場者数</v-subheader>
                  </v-col>

                  <v-col cols="6">
                    <v-subheader>本日の退場者数</v-subheader>
                  </v-col>
                </v-row>
                
                <v-row>
                  <v-col cols="6">
                    <v-text-field
                      name="count_enter"
                      type="text"
                      suffix="名"
                      v-model="count_info.count_enter"
                      readonly
                      solo
                    >
                    </v-text-field>
                  </v-col>
                  <v-col cols="6">
                    <v-text-field
                      name="count_exit"
                      type="text"
                      suffix="名"
                      v-model="count_info.count_exit"
                      readonly
                      solo
                    >
                    </v-text-field>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col cols="6">
                    <v-subheader>今場内にいる人数</v-subheader>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col cols="6">
                    <v-text-field
                      name="count_inside"
                      type="text"
                      suffix="名"
                      v-model="count_info.count_inside"
                      readonly
                      solo
                    >
                    </v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-alert
                      outlined
                      prominent
                      text
                      type="success"
                      v-if="count_info.has_blacklist == false"
                    >
                      ブラックリスト未検出
                    </v-alert>
                    <v-alert
                      outlined
                      prominent
                      text
                      type="error"
                      v-else
                    >
                      ブラックリスト検出
                      <v-icon
                        slot="append"
                        @click="deleteItem()"
                      >
                        mdi-timer-off-outline
                      </v-icon>
                    </v-alert>
                  </v-col>
                </v-row>

              </v-card-text>
          </v-card>
        </v-layout>

        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5 justify-center">当施設のアラームを解消しますか？</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">キャンセル</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">確定</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>

      </v-container>
   </v-app>
</template>

<script>
export default {
  // props: {
  //   user_id: String,
  //   building_id: String,
  //   callback: Function,
  // },

  data: () => ({
    name: '現場確認',
    dialogDelete: false,
    loginItem: {
      user_id: null,
      building_id: null,
    },
    count_info: {
      name: null,
      to_user: null,
      count_enter: null,
      count_exit: null,
      count_inside: null,
      has_blacklist: null,
      detail: null,
    },
  }),

  created () {
    this.initialize()
  },

  methods: {
    initialize () {
      // Login成功の場合、取得したデータで初期化する
      let count_info = this.$route.query.count_info

      // URLでの直接アクセスは禁止にする
      if (typeof(count_info) == "undefined") {
        // 跳转到登录页面
        this.$router.push('/login')
        return
      }
      this.count_info = count_info
    },

    async clearAlarm (item) {
      await this.$axios({
        method: 'post',
        url: '/api/clear_alarm_by_building_name',
        withCredentials: true,
        data: JSON.stringify(item)
      }).then((res) => {
        console.log(res)
      })
    },

    deleteItem () {
      this.dialogDelete = true
    },

    deleteItemConfirm () {
      // 找到该设施的所有device，更新最近警报时间
      this.clearAlarm({ "building_name": this.count_info.name })

      // clear alarm in frontend table
      this.count_info.has_blacklist = false
      this.closeDelete()
    },

    closeDelete () {
      this.dialogDelete = false
    },
  },
};
</script>

<style></style>
