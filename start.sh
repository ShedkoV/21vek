#!/bin/sh

uvicorn app.service:app --host 0.0.0.0 --port 8000 --reload
