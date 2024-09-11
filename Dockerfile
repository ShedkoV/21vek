FROM python:3.9

# Устанавливаем зависимости Poetry
RUN pip install poetry

# Копируем poetry.lock и pyproject.toml
COPY poetry.lock pyproject.toml ./

# Устанавливаем зависимости проекта
RUN poetry install --no-dev

# Копируем файлы проекта
COPY src/ ./src/

# Запускаем сервис FastAPI (только одна команда CMD)
CMD ["uvicorn", "src.app.service:app", "--host", "0.0.0.0", "--port", "8000"]
