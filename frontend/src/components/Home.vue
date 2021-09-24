<template>

  <v-card>
    <v-card-title>
      <span class="text-h5">{{ "Inflow" }}</span>
    </v-card-title>

    <v-card-text>
      <v-container>
        <v-row>
          <v-col
            cols="12"
          >
            <v-sparkline
              :value="value_in"
              :gradient="gradient"
              :smooth="radius || false"
              :padding="padding"
              :line-width="width"
              :stroke-linecap="lineCap"
              :gradient-direction="gradientDirection"
              :fill="fill"
              :type="type"
              :auto-line-width="autoLineWidth"
              auto-draw
            ></v-sparkline>
          </v-col>
        </v-row>
      </v-container>
    </v-card-text>
  

    <v-card-title>
      <span class="text-h5">{{ "Outflow" }}</span>
    </v-card-title>

    <v-sheet
      class="v-sheet--offset mx-auto"
      color="cyan"
      elevation="12"
      max-width="calc(100% - 32px)"
    >
      <v-sparkline
        :labels="labels"
        :value="value_out"
        color="white"
        line-width="2"
        padding="16"
      ></v-sparkline>
    </v-sheet>

    <v-card-text class="pt-0">
      <div class="text-h6 font-weight-light mb-2">
        User Registrations
      </div>
      <div class="subheading font-weight-light grey--text">
        Last Campaign Performance
      </div>
      <v-divider class="my-2"></v-divider>
      <v-icon
        class="mr-2"
        small
      >
        mdi-clock
      </v-icon>
      <span class="text-caption grey--text font-weight-light">last registration 26 minutes ago</span>
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="primary" @click="exportPdf()">PDFを出力する</v-btn>
    </v-card-actions>

  </v-card>

</template>

<script>
  const gradients = [
    ['#222'],
    ['#42b3f4'],
    ['red', 'orange', 'yellow'],
    ['purple', 'violet'],
    ['#00c6ff', '#F0F', '#FF0'],
    ['#f72047', '#ffd200', '#1feaea'],
  ]
    
  export default {
    name: 'Home',

    data: () => ({
      width: 2,
      radius: 10,
      padding: 8,
      lineCap: 'round',
      gradient: gradients[5],
      value_in: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0],
      gradientDirection: 'top',
      gradients,
      fill: false,
      type: 'trend',
      autoLineWidth: false,

      labels: [
        '12am',
        '3am',
        '6am',
        '9am',
        '12pm',
        '3pm',
        '6pm',
        '9pm',
      ],
      value_out: [
        200,
        675,
        410,
        390,
        310,
        460,
        250,
        240,
      ],
    }),

    methods: {

      downloadFile (response, filename) {
        // It is necessary to create a new blob object with mime-type explicitly set
        // otherwise only Chrome works like it should
        var newBlob = new Blob([response.data], {type: 'application/pdf'})

        // IE doesn't allow using a blob object directly as link href
        // instead it is necessary to use msSaveOrOpenBlob
        if (window.navigator && window.navigator.msSaveOrOpenBlob) {
          window.navigator.msSaveOrOpenBlob(newBlob)
          return
        }

        // For other browsers:
        // Create a link pointing to the ObjectURL containing the blob.
        const data = window.URL.createObjectURL(newBlob)
        var link = document.createElement('a')
        link.href = data
        link.download = filename + '.pdf'
        link.click()
        setTimeout(function () {
          // For Firefox it is necessary to delay revoking the ObjectURL
          window.URL.revokeObjectURL(data)
        }, 100)
      },

      async exportPdf () {
        await this.$axios({
          method: 'post',
          url: '/api/report',
          // data: JSON.stringify(item),
          responseType: 'blob'   // blobを設定しないとPDFは空白になる
        }).then((response) => {

          // Method 1: 直接にダウンロードする
          // this.downloadFile(response, 'report')
          
          // Method 2: 新しいウィンドウでPDFを開く
          const blob = new Blob([response.data], { type: response.data.type })
          console.log(blob)

          // Build a URL from the blob
          const link = URL.createObjectURL(blob);
          // Open the URL on new Window
          window.open(link);
        })
        .catch(error => {
            console.log(error)
        })
      },
    },

  }
</script>
