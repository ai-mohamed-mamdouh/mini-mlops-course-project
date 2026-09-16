FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./

COPY src ./src
COPY artifacts ./artifacts

RUN pip install uv \
    && uv sync --frozen

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "mini_mlopscourse_project.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]