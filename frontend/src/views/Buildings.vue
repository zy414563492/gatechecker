<template>
  <v-app>
    
    <link-bar :subLink="name"/>

    <v-data-table
      :headers="headers"
      :items="buildings"
      class="elevation-1"
    >
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
                施設を追加
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
                        v-model="editedItem.building_id"
                        label="施設ID"
                        outlined
                      ></v-text-field>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col
                      cols="12"
                    >
                      <v-text-field
                        v-model="editedItem.name"
                        label="名称"
                        outlined
                      ></v-text-field>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col
                      cols="12"
                    >
                      <v-text-field
                        v-model="editedItem.location"
                        label="アドレス"
                        outlined
                      ></v-text-field>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col
                      cols="12"
                    >
                      <v-select
                        v-model="editedItem.to_user"
                        :items="users"
                        label="所属ユーザー"
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
      name: '施設',
      dialog: false,
      dialogDelete: false,
      headers: [
        { text: '施設ID', value: 'building_id' },
        { text: '名称', value: 'name' },
        { text: 'アドレス', value: 'location' },
        { text: '所属ユーザー', value: 'to_user' },
        { text: '操作', value: 'actions', sortable: false },
      ],
      users: [],
      buildings: [],
      editedIndex: -1,
      editedItem: {
        building_id: null,
        name: null,
        location: null,
        to_user: null,
      },
      defaultItem: {
        building_id: null,
        name: null,
        location: null,
        to_user: null,
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? '施設を追加' : '施設を更新'
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
      this.getUsers()
    },

    methods: {
      async initialize () {
        await this.$axios
        .post('/api/get_buildings')
        .then((res) => {
          console.log(res.data)
          this.buildings = res.data.building_list
        })
        .catch(err => console.log(err))
      },

      async addBuilding (item) {
        await this.$axios({
          method: 'post',
          url: '/api/add_building',
          withCredentials: true,
          data: JSON.stringify(item)
        }).then((res) => {
          console.log(res)
        })
      },

      async removeBuilding (item) {
        await this.$axios({
          method: 'post',
          url: '/api/remove_building',
          withCredentials: true,
          data: JSON.stringify(item)
        }).then((res) => {
          console.log(res)
        })
      },

      // 所属ユーザーの選択肢を取得する
      async getUsers () {
        await this.$axios
        .post('/api/get_users_id')
        .then((res) => {
          console.log(res.data)
          this.users = res.data.users
        })
        .catch(err => console.log(err))
      },

      editItem (item) {
        this.editedIndex = this.buildings.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.buildings.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        // remove from database
        this.removeBuilding(this.editedItem)

        // remove from frontend table
        this.buildings.splice(this.editedIndex, 1)
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
          Object.assign(this.buildings[this.editedIndex], this.editedItem)
        } else {
          this.buildings.push(this.editedItem)
        }
        // エンドユーザーの追加
        this.addBuilding(this.editedItem)

        this.close()
      },
    },
  }
</script>