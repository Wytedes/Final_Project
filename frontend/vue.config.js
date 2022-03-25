const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false, //关闭语法检查
  devServer:{
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        pathRewrite: {
          '^/api': ''
        },
        ws: true, //用于支持websocket
        changeOrigin:true, //跨域，用于控制请求头中的host值
      }
    }
  }
})
