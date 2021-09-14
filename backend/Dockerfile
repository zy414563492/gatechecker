# 参考)https://www.dusaiphoto.com/article/74/

# 从仓库拉取 带有 python 3.7 的 Linux 环境
FROM python:3.7

# 创建 app 文件夹并将其设置为工作目录
RUN mkdir /app
WORKDIR /app

EXPOSE 80
EXPOSE 443

# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

# 更新 pip
RUN pip install pip -U

# 将 requirements.txt 复制到容器的 app 目录
ADD requirements.txt /app/

# 安装django
RUN pip install django==2.2

# 安装库
RUN pip install -r requirements.txt

# 将当前目录复制到容器的 app 目录
ADD . /app/