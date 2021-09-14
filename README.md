Gatechecker
================================================================

## Docker Composeによる起動

```
docker-compose build --no-cache
docker-compose up
```

ポート8080でフロントエンドにアクセスできます。
なお、 `docker-compose up`が失敗する場合は、過去のデータが残っている可能性があります。消しましょう。
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

