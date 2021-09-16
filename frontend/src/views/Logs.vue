<template>
  <v-app>
    
    <link-bar :subLink="name"/>

    <v-data-table
      :headers="headers"
      :items="logs"
      class="elevation-1"
    >
      <template v-slot:[`item.temperature`]="{ item }">
        <v-chip
          :color="getColor(item.temperature)"
          dark
        >
          {{ item.temperature }}
        </v-chip>
      </template>

      <template v-slot:[`item.is_blacklist`]="{ item }">
        <v-icon
          :color="getIconColor(item.is_blacklist)"
          class="mr-2"
        >
          {{ item.is_blacklist ? "mdi-alert-decagram" : "mdi-check-circle-outline"}}
        </v-icon>
      </template>
      
      <template v-slot:top>
        <v-toolbar
          flat
        >
          <v-toolbar-title>{{ name }}</v-toolbar-title>
          <v-divider
            class="mx-4"
            inset
            vertical
          ></v-divider>
          <v-spacer></v-spacer>
          <v-dialog
            v-model="dialog"
            max-width="500px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="warning"
                dark
                class="mb-2"
                v-bind="attrs"
                v-on="on"
              >
                模擬検温記録を追加
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                      cols="12"
                    >
                      <v-select
                        v-model="editedItem.to_device"
                        :items="devices"
                        label="デバイスID"
                        outlined
                      ></v-select>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col
                      cols="12"
                    >
                      <v-text-field
                        v-model="editedItem.log_id"
                        label="ログID"
                        outlined
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col
                      cols="12"
                    >
                      <v-text-field
                        v-model="editedItem.time"
                        label="時間"
                        outlined
                        :hint="'例: ' + getdateTime()"
                        persistent-hint
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col
                      cols="12"
                    >
                      <v-text-field
                        v-model="editedItem.temperature"
                        label="体温"
                        outlined
                        type="number"
                        max="50"
                        min="30"
                        step="0.1"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col
                      cols="12"
                    >
                      <v-select
                        v-model="editedItem.is_blacklist"
                        :items="blacklist_state"
                        item-text="state_name"
                        item-value="state"
                        label="ブラックリスト検出"
                        outlined
                      >
                        <template slot='selection' slot-scope='{ item }'>
                          <v-icon
                            :color="getIconColor(item.state)"
                            class="mr-2"
                          >
                            {{ item.state ? "mdi-alert-decagram" : "mdi-check-circle-outline"}}
                          </v-icon>
                        </template>
                        
                        <template slot='item' slot-scope='{ item }'>
                          <v-icon
                            :color="getIconColor(item.state)"
                            class="mr-2"
                          >
                            {{ item.state ? "mdi-alert-decagram" : "mdi-check-circle-outline"}}
                          </v-icon>
                        </template>

                      </v-select>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="close"
                >
                  キャンセル
                </v-btn>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="save"
                >
                  保存
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5 justify-center">このアイテムを削除しますか？</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete">キャンセル</v-btn>
                <v-btn color="blue darken-1" text @click="deleteItemConfirm">確定</v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <!-- <template v-slot:item.actions="{ item }"> -->
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon
          small
          class="mr-2"
          @click="editItem(item)"
        >
          mdi-pencil
        </v-icon>
        <v-icon
          small
          @click="deleteItem(item)"
        >
          mdi-delete
        </v-icon>
      </template>
      <template v-slot:no-data>
        <v-progress-circular
          indeterminate
          color="primary"
        ></v-progress-circular>
      </template>
    </v-data-table>
  </v-app>
</template>

<script>
  export default {
    data: () => ({
      name: '検温記録',
      dialog: false,
      dialogDelete: false,
      headers: [
        { text: 'デバイスID', value: 'to_device' },
        { text: 'ログID', value: 'log_id' },
        { text: '時間', value: 'time' },
        { text: '体温', value: 'temperature' },
        { text: 'ブラックリスト検出', value: 'is_blacklist' },
        { text: '操作', value: 'actions', sortable: false },
      ],
      devices: [],
      logs: [],
      blacklist_state: [
        { state: true, state_name: '◯' },
        { state: false, state_name: '✖️' }
      ],
      editedIndex: -1,
      editedItem: {
        to_device: null,
        log_id: null,
        time: null,
        temperature: null,
        is_blacklist: false,
      },
      defaultItem: {
        to_device: null,
        log_id: null,
        time: null,
        temperature: null,
        is_blacklist: false,
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? '模擬検温記録を追加' : '模擬検温記録を更新'
        // return 'New Item'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
      this.initialize()
      this.getDevices()
    },

    methods: {
      async initialize () {
        await this.$axios
        .post('/api/get_logs')
        .then((res) => {
          console.log(res.data)
          this.logs = res.data.log_list
        })
        .catch(err => console.log(err))
      },

      async addLog (item) {
        await this.$axios({
          method: 'post',
          url: '/api/add_log',
          withCredentials: true,
          data: JSON.stringify(item)
        }).then((res) => {
          console.log(res)
        })
      },

      async removeLog (item) {
        await this.$axios({
          method: 'post',
          url: '/api/remove_log',
          withCredentials: true,
          data: JSON.stringify(item)
        }).then((res) => {
          console.log(res)
        })
      },

      // 所属デバイスの選択肢を取得する
      async getDevices () {
        await this.$axios
        .post('/api/get_devices_id')
        .then((res) => {
          console.log(res.data)
          this.devices = res.data.devices
        })
        .catch(err => console.log(err))
      },

      // get current time
      getdateTime () {
        var _this = this;
        let yy = new Date().getFullYear();
        let mm = new Date().getMonth() + 1;
        let dd = new Date().getDate();
        let hh = new Date().getHours();
        let mf =
          new Date().getMinutes() < 10
            ? "0" + new Date().getMinutes()
            : new Date().getMinutes();
        let ss =
          new Date().getSeconds() < 10
            ? "0" + new Date().getSeconds()
            : new Date().getSeconds();
        let gettime = yy + "-" + mm + "-" + dd + " " + hh + ":" + mf + ":" + ss;
        return gettime;
      },

      getColor (temperature) {
        if (temperature > 37.5) return 'red'
        else if (temperature > 37.0) return 'orange'
        else return 'green'
      },

      getIconColor (is_blacklist) {
        if (is_blacklist) return 'red'
        else return 'green'
      },

      editItem (item) {
        this.editedIndex = this.logs.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.logs.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        // remove from database
        this.removeLog(this.editedItem)

        // remove from frontend table
        this.logs.splice(this.editedIndex, 1)
        this.closeDelete()
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.logs[this.editedIndex], this.editedItem)
        } else {
          this.logs.push(this.editedItem)
        }
        // デバイスの追加
        this.addLog(this.editedItem)

        this.close()
      },
    },
  }
</script>