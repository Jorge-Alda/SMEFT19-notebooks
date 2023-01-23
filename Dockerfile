FROM python:3.9-slim

WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin/"

COPY apt.txt pyproject.toml poetry.lock /app/

RUN apt update -y && \ 
    apt install -y --no-install-recommends $(cat /app/apt.txt) && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    poetry config virtualenvs.create false && \
    poetry install

CMD ["bash"]