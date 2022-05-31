# FastAPI + React

FastAPI+React のアプリケーションサンプルです。
本の検索サイトをイメージして構築しています。

## 技術構成要素

### Backend

|                      |                                                   |
| :------------------- | :------------------------------------------------ |
| 言語                 | Python 3                                          |
| FW                   | [FastAPI](https://fastapi.tiangolo.com/)          |
| パッケージマネージャ | [Poetry](https://github.com/python-poetry/poetry) |
| Formatter            | [black](https://black.readthedocs.io/en/stable/)  |
| Linter               | [Flake8](https://flake8.pycqa.org/en/latest/)     |
| Database Tool        | [SQLAlchemy](https://www.sqlalchemy.org/)         |

### Frontend

|                  |                                                     |
| :--------------- | :-------------------------------------------------- |
| 言語             | TypeScript                                          |
| FW               | [React](https://ja.reactjs.org/)                    |
| BuildTool        | [vite](https://vitejs.dev/)                         |
| Formatter        | [Prettier](https://black.readthedocs.io/en/stable/) |
| Linter           | [ESLint](https://flake8.pycqa.org/en/latest/)       |
| Http Client      | [axios](https://axios-http.com/)                    |
|                  | [Aspida](https://github.com/aspida/aspida)          |
|                  | [SWR](https://swr.vercel.app/ja)                    |
| Router           | [React Router]()                                    |
| State Management | TODO                                                |
| Design Framework | [Ant Design](https://ant.design/)                   |
| CSS Library      | [Tailwindcss](https://tailwindcss.com/)             |

## 起動方法

```sh
$ docker compose up -d
```

それぞれ以下のポートで立ち上がります

- backend: http://localhost:8000
- frontend: http://localhost:3000
- Opensearch Dashboard: http://localhost:5601
  - admin/admin

### Opensearch へのデータ投入方法

```
$ cd migrations/search-engine
$ sh migration.sh
```

### DB のマイグレーション

TODO

## 開発環境構築手順

Backend, Frontend 共に `VSCode Remote Containers` を使用することを想定しています。

## Requirements

- Docker
- VSCode
  - 拡張機能: Remote - Containers

### 開発の仕方

1. `api` `front` ディレクトリを VSCode で開く
2. 右下に `Folder contains a Dev Container configuration file. Reopen folder to develop in a container` と表示されるので、`Reopen in container` を選択する
3. Container 内で VSCode が起動するので普通に開発を行う
