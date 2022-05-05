FROM python:3.9

EXPOSE 2007

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

CMD ["python", "/code/src/main.py"]


