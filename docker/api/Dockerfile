FROM python:3.10.4-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /api

# pipを使ってpoetryをインストール
RUN pip install poetry

# 
RUN poetry config virtualenvs.in-project true
