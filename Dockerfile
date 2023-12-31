# 使用 Python 3.9 作为基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 将目下的所有文件复制到容器的 /app 目录下
COPY . /app

# 安装依赖
RUN pip install -r requirements.txt

# 运行 Python 脚本
CMD ["python", "main.py"]
