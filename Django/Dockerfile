FROM python:3.11

RUN apt-get update && apt-get install -y --no-install-recommends netcat-traditional
RUN apt-get autoremove -y
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.4.2

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /usr/src/app/api

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . .

RUN chmod +x ./entrypoint.sh

# FROM development as production

# ENV DATABASE_HOST=db
# COPY . ./
# RUN chmod +x ./wait_db.sh

# ENTRYPOINT [ "sh", "./entrypoint.sh" ]
