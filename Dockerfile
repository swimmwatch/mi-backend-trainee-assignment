FROM python:3.9

WORKDIR /app

# Install poetry
RUN apt install curl
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH /root/.local/bin:$PATH

COPY poetry.lock .
COPY pyproject.toml .

# Install Python dependecies
RUN poetry install --no-dev

COPY . .