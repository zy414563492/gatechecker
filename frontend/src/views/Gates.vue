<template>
  <v-app>
    
    <link-bar :subLink="name"/>

    <v-data-table
      :headers="headers"
      :items="gates"
      class="elevation-1"
    >
      <template v-slot:[`item.is_open`]="{ item }">
        <v-chip
          :color="getColor(item.is_open)"
          dark
        >
          {{ item.is_open ? 'Opening' : 'Closed'}}
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
                ゲートを追加
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
                        v-model="editedItem.gate_id"
                        label="ゲートID"
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
                      <v-select
                        v-model="editedItem.is_open"
                        :items="gate_state"
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
                      <v-select
                        v-model="editedItem.to_building"
                        :items="buildings"
                        label="所属施設"
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
      name: 'ゲート',
      dialog: false,
      dialogDelete: false,
      headers: [
        { text: 'ゲートID', value: 'gate_id' },
        { text: '名称', value: 'name' },
        { text: '状態', value: 'is_open' },
        { text: '所属施設', value: 'to_building' },
        { text: '操作', value: 'actions', sortable: false },
      ],
      buildings: [],
      gates: [],
      gate_state: [
        {state: true, state_name:'Opening'},
        {state: false, state_name:'Closed'}
      ],
      editedIndex: -1,
      editedItem: {
        gate_id: null,
        name: null,
        is_open: true,
        to_building: null,
      },
      defaultItem: {
        gate_id: null,
        name: null,
        is_open: true,
        to_building: null,
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'ゲートを追加' : 'ゲートを更新'
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
      this.getBuildings()
    },

    methods: {
      async initialize () {
        await this.$axios
        .post('/api/get_gates')
        .then((res) => {
          console.log(res.data)
          this.gates = res.data.gate_list
        })
        .catch(err => console.log(err))
      },

      async addGate (item) {
        await this.$axios({
          method: 'post',
          url: '/api/add_gate',
          withCredentials: true,
          data: JSON.stringify(item)
        }).then((res) => {
          console.log(res)
        })
      },

      async removeGate (item) {
        await this.$axios({
          method: 'post',
          url: '/api/remove_gate',
          withCredentials: true,
          data: JSON.stringify(item)
        }).then((res) => {
          console.log(res)
        })
      },

      // 所属施設の選択肢を取得する
      async getBuildings () {
        await this.$axios
        .post('/api/get_buildings_id')
        .then((res) => {
          console.log(res.data)
          this.buildings = res.data.buildings
        })
        .catch(err => console.log(err))
      },

      getColor (gate_state) {
        if (gate_state) return 'green'
        else return 'red'
      },

      editItem (item) {
        this.editedIndex = this.gates.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.gates.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        // remove from database
        this.removeGate(this.editedItem)

        // remove from frontend table
        this.gates.splice(this.editedIndex, 1)
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
          Object.assign(this.gates[this.editedIndex], this.editedItem)
        } else {
          this.gates.push(this.editedItem)
        }
        // ゲートの追加
        this.addGate(this.editedItem)

        this.close()
      },
    },
  }
</script>