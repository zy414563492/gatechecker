<template>
  <v-app>
    
    <link-bar :subLink="name"/>

    <v-data-table
      :headers="headers"
      :items="devices"
      class="elevation-1"
    >
      <template v-slot:[`item.is_entrance`]="{ item }">
        {{ item.is_entrance ? '入口' : '出口'}}
      </template>

      <template v-slot:[`item.is_using`]="{ item }">
        <v-chip
          :color="getColor(item.is_using)"
          dark
        >
          {{ item.is_using ? '使用中' : '一時停止' }}
        </v-chip>
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
                color="primary"
                dark
                class="mb-2"
                v-bind="attrs"
                v-on="on"
              >
                デバイスを追加
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
                      <v-text-field
                        v-model="editedItem.device_id"
                        label="デバイスID"
                        outlined
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  
                  <v-row>
                    <v-col
                      cols="12"
                    >
                      <v-select
                        v-model="editedItem.is_entrance"
                        :items="direction"
                        item-text="state_name"
                        item-value="state"
                        label="向き"
                        outlined
                      ></v-select>

                    </v-col>
                  </v-row>
                  
                  <v-row>
                    <v-col
                      cols="12"
                    >
                      <v-select
                        v-model="editedItem.is_using"
                        :items="device_state"
                        item-text="state_name"
                        item-value="state"
                        label="状態"
                        outlined
                      ></v-select>

                    </v-col>
                  </v-row>
                  
                  <v-row>
                    <v-col
                      cols="12"
                    >
                      <v-text-field
                        v-model="editedItem.last_alert_time"
                        label="最近のアラート時間"
                        outlined
                      ></v-text-field>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col
                      cols="12"
                    >
                      <v-select
                        v-model="editedItem.to_gate"
                        :items="gates"
                        label="所属ゲート"
                        outlined
                      ></v-select>
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
      name: 'デバイス',
      dialog: false,
      dialogDelete: false,
      headers: [
        { text: 'デバイスID', value: 'device_id' },
        { text: '向き', value: 'is_entrance' },
        { text: '状態', value: 'is_using' },
        { text: '最近のアラート時間', value: 'last_alert_time' },
        { text: '所属ゲート', value: 'to_gate' },
        { text: '操作', value: 'actions', sortable: false },
      ],
      gates: [],
      devices: [],
      direction: [
        {state: true, state_name:'入口'},
        {state: false, state_name:'出口'}
      ],
      device_state: [
        {state: true, state_name:'使用中'},
        {state: false, state_name:'一時停止'}
      ],
      editedIndex: -1,
      editedItem: {
        device_id: null,
        is_entrance: true,
        is_using: true,
        last_alert_time: null,
        to_gate: null,
      },
      defaultItem: {
        device_id: null,
        is_entrance: true,
        is_using: true,
        last_alert_time: null,
        to_gate: null,
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'デバイスを追加' : 'デバイスを更新'
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
      this.getGates()
    },

    methods: {
      async initialize () {
        await this.$axios
        .post('/api/get_devices')
        .then((res) => {
          console.log(res.data)
          this.devices = res.data.device_list
        })
        .catch(err => console.log(err))
      },

      async addDevice (item) {
        await this.$axios({
          method: 'post',
          url: '/api/add_device',
          withCredentials: true,
          data: JSON.stringify(item)
        }).then((res) => {
          console.log(res)
        })
      },

      async removeDevice (item) {
        await this.$axios({
          method: 'post',
          url: '/api/remove_device',
          withCredentials: true,
          data: JSON.stringify(item)
        }).then((res) => {
          console.log(res)
        })
      },

      // 所属ゲートの選択肢を取得する
      async getGates () {
        await this.$axios
        .post('/api/get_gates_id')
        .then((res) => {
          console.log(res.data)
          this.gates = res.data.gates
        })
        .catch(err => console.log(err))
      },

      getColor (gate_state) {
        if (gate_state) return 'green'
        else return 'red'
      },

      editItem (item) {
        this.editedIndex = this.devices.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.devices.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        // remove from database
        this.removeDevice(this.editedItem)

        // remove from frontend table
        this.devices.splice(this.editedIndex, 1)
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
          Object.assign(this.devices[this.editedIndex], this.editedItem)
        } else {
          this.devices.push(this.editedItem)
        }
        // デバイスの追加
        this.addDevice(this.editedItem)

        this.close()
      },
    },
  }
</script>