# makefile
DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
LOCAL_FILE = docker-compose.local.yml
STORAGES_FILE = docker_compose/storages.yaml
APP_CONTAINER = mir-bot
SERVICE_NAME = mir-bot


.PHONY: app-sync
app-sync:  #
	@uv sync

.PHONY: app-logs
app-logs:  # запускает приложение с логами в консоли
	@$(MAKE) app-sync
	@${DC} -f ${LOCAL_FILE} up --build

.PHONY: app
app:  # запускает приложение и применяет все миграции
	@${DC} -f ${LOCAL_FILE} up --build -d
	@$(MAKE) migrate-up

.PHONY: app-down
app-down:
	@${DC} -f ${LOCAL_FILE} down

# Создать миграцию
.PHONY: migrate # make migrate m="add users table"
migrate:
	@${DC} -f ${LOCAL_FILE} exec ${SERVICE_NAME} alembic revision --autogenerate -m "$(m)"

# Применить миграции
.PHONY: migrate-up  # make migrate-up
migrate-up:
	@${DC} -f ${LOCAL_FILE} exec ${SERVICE_NAME} alembic upgrade head

# Откатить миграцию
.PHONY: migrate-down  # make migrate-down
migrate-down:
	@${DC} -f ${LOCAL_FILE} exec ${SERVICE_NAME} alembic downgrade -1
