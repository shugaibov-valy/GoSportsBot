FROM python:3.8-alpine
# Используем alpine, так как он весит меньше
# Немного информации о контейнере 
# Надо для питонских модулей
RUN apk add gcc
RUN apk add nano
RUN apk add g++
RUN apk add musl-dev
COPY . /Bot/
WORKDIR /Bot
# Ставим модули
RUN pip3 install -r requirements.txt

# Наконец, запускаем сервер 
CMD ["python3", "main.py"]
