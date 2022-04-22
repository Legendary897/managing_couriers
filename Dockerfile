FROM python:3-onbuild

EXPOSE 2007

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./apps /code/apps

COPY ./routers /code/routers

COPY ./server_config /code/server_config

COPY ./init_application.py /code/init_application.py

COPY ./server.py /code/server.py

CMD ["python3", "/code/server.py"]


