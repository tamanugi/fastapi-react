FROM python:3.10.4-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /api

# pipを使ってpoetryをインストール
RUN pip install poetry

# uvicornのサーバーを立ち上げる
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
