FROM python:3
RUN apt-get update  && apt-get install -y python3-dev default-libmysqlclient-dev build-essential
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install mysqlclient pymysql
COPY . .
EXPOSE 8000

