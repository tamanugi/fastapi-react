#!/bin/bash

poetry install
poetry run uvicorn app.main:app --host 0.0.0.0 --reload
