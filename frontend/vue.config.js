module.exports = {
  transpileDependencies: [
    'vuetify'
  ],
  chainWebpack: config => {
    config.module.rules.delete('eslint');
  },
  // devServer: {
  //   proxy: {
  //     '^/api': {
  //       target: 'http://backend',
  //       port: 8000,
  //       secure: false,
  //       pathRewrite:{
  //          '^/api/*': '',
  //       }
  //     }
  //   }
  // },
}
