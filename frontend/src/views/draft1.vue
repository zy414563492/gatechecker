<template>
  <div>
    <v-card>
      <v-card-title>
          エンドユーザー
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="user_list"
        :items-per-page="10"
        class="elevation-1"
        :search="search"
      ></v-data-table>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'endusers',
  data () {
    return {
      search: '',
      headers: [
        { text: 'ユーザーID', value: 'user_id' },
        { text: '名称', value: 'name' },
      ],
      user_list: [],
    }
  },
  methods: {
    show_users () {
      this.$axios
        .post('http://localhost:8000/gatechecker/get_users')
        .then((res) => {
          console.log(res.data)
          this.user_list = res.data.user_list
        })
        .catch(err => console.log(err))
    }
  },
  mounted(){
    this.show_users()
  }
}
</script>
