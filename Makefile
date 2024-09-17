APP_NAME = app 
DOCKER_COMPOSE  = docker-compose
DOCKER_COMPOSE_FILE = docker-compose.yml


.PHONY: build up down restart logs shell test

build:
	${DOCKER_COMPOSE} -f ${DOCKER_COMPOSE_FILE} build

up:
	${DOCKER_COMPOSE} -f ${DOCKER_COMPOSE_FILE} up

down:
	${DOCKER_COMPOSE} -f ${DOCKER_COMPOSE_FILE} down

restart:
	${DOCKER_COMPOSE} -f ${DOCKER_COMPOSE_FILE} down && ${DOCKER_COMPOSE} -f ${DOCKER_COMPOSE_FILE} up

logs:
	${DOCKER_COMPOSE} -f ${DOCKER_COMPOSE_FILE} logs -f

shell:
	${DOCKER_COMPOSE} -f ${DOCKER_COMPOSE_FILE} exec ${APP_NAME} /bin/bash

test:
	${DOCKER_COMPOSE} -f ${DOCKER_COMPOSE_FILE} exec ${APP_NAME} pytest