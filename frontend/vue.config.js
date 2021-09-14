module.exports = {
  transpileDependencies: [
    'vuetify'
  ],
  chainWebpack: config => {
    config.module.rules.delete('eslint');
  },
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000/gatechecker',
        // secure: false,
        // port: 8080,
        // disableHostCheck: true,
        // changeOrigin: true,
        pathRewrite:{
           '^/api': '',
        }
      }
    }
  },
}
