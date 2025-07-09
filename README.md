# sentiment_api_flask
A REST API service for my new job
 __________________________________
# NO DOCKER VERSION (no venv, global environment, как в задании) 
__________________________________

bash
  cd with_docker/src/
  
  pip install flask

  python main.py



__________________________________
# DOCKER VERSION (isolated docker environment, не как в задании, мой доп)
__________________________________
bash 
0. Перейти в папку с докер инструкцией (структура папок в репо сделана просто для наглядности)

cd with_docker/src/

1. Собрать контейнер

  docker build -t review_app .

2.  Запустить

  docker run --rm review_app

__________________________________
# DOCKER COMPOSE VERSION..... (build containers via 1 command ) 
__________________________________
I could have done it... 
Запускалось бы docker compose up 
(--build для пересборки, -d detached) 
Шатдаунилось - docker compose down
Я в 99 процентах случаев использую именно такой вариант

Через обычный докер build я обычно не запускаю
