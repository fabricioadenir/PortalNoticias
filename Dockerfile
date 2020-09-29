FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /portal-noticias
WORKDIR /portal-noticias
ADD requirements.txt /portal-noticias/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install --upgrade djongo
ADD . /portal-noticias/
