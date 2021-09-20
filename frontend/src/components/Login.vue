<template>
   <v-app>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>
              <v-card class="elevation-12">
                  <v-toolbar dark color="primary">
                    <v-toolbar-title>{{ name }}</v-toolbar-title>
                  </v-toolbar>
                  <v-card-text>
                    <v-form>
                      <!-- 方法１ -->
                      <v-text-field
                        prepend-icon="mdi-account"
                        name="user_id"
                        label="ユーザーID"
                        type="text"
                        v-model="user_id"
                      ></v-text-field>
                      
                      <!-- 方法２ -->
                      <v-text-field
                        name="building_id"
                        label="施設ID"
                        type="text"
                        v-model="building_id"
                      >
                        <v-icon
                          slot="prepend"
                        >
                          mdi-office-building-marker
                        </v-icon>
                      </v-text-field>
                      <v-alert
                        dense
                        outlined
                        type="error"
                        border="left"
                        v-if="error_flg"
                      >
                        {{ error_msg }}
                      </v-alert>
                    </v-form>
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" @click="login">現場確認</v-btn>
                  </v-card-actions>
              </v-card>
            </v-flex>
        </v-layout>
      </v-container>
   </v-app>
</template>

<script>
import store from '../store'

export default {
  props: {
    source: String,
  },

  data: () => ({
    name: 'Login',
    user_id: null,
    building_id: null,
    error_flg: false,
    error_msg: null,
  }),

  methods: {
    login () {
      // 一些其他校验及其他操作，如校验用户名密码是否为空
  
      // 请求登陆接口
      this.$axios.post('/api/get_count_single', {
        user_id: this.user_id,
        building_id: this.building_id,
      })
        .then(res => {
          // 登陆成功相关操作
          if (res.data.status == 'success') {
            let count_info = res.data.count_info
            console.log(count_info)

            // console.log("Get Logged")
            // store.commit('validAuth')

            // 跳转到结果页面
            this.$router.push({
              path: '/result',
              query: {
                count_info: count_info,
              },
            })
          }
          else {
            // 登录失败，不跳转并提示错误
            this.error_flg = true
            this.error_msg = res.data.error_msg
            console.log(this.error_msg)
          }
        })
        .catch(err => {
          console.log('Failed to connect with MySQL')
        })
      },
    },
};
</script>

<style></style>
