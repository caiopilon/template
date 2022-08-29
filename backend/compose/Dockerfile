FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* .

ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

COPY ./compose/scripts/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/scripts/start_api /start_api
RUN sed -i 's/\r$//g' /start_api
RUN chmod +x /start_api

COPY ./compose/scripts/start_worker /start_worker
RUN sed -i 's/\r$//g' /start_worker
RUN chmod +x /start_worker

COPY ./compose/scripts/start_beat /start_beat
RUN sed -i 's/\r$//g' /start_beat
RUN chmod +x /start_beat

COPY ./compose/scripts/start_flower /start_flower
RUN sed -i 's/\r$//g' /start_flower
RUN chmod +x /start_flower

# ENTRYPOINT ["/entrypoint"]