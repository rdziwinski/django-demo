# Import base image
FROM python:3.9-bullseye as build-stage

# Instalacja niezbędnych paczek
RUN apt-get update && apt-get install --no-install-recommends -y build-essential libpq-dev

# Kopiujemy plik z wymaganymi paczkami PIP
COPY ./requirements.txt /app/requirements.txt

RUN python3 -m pip install -r /app/requirements.txt

# nowy stage

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN addgroup --system django && adduser --system --ingroup django django

COPY --chown=django:django ./compose/production/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY --chown=django:django ./compose/production/start /start
RUN chmod +x /start

COPY --chown=django:django ./myproject/ /app/

USER django
WORKDIR /app
CMD /start
ENTRYPOINT ["/entrypoint"]


