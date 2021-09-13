# 参考) https://jp.vuejs.org/v2/cookbook/dockerize-vuejs-app.html
# 参考) https://mincong.io/cn/packing-a-vue-js-project-using-docker-and-nginx/

# ビルド環境
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# 本番環境
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]