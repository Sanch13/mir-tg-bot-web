# makefile
DC = docker compose
D = docker
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
LOCAL_FILE = docker-compose.local.yml
STORAGES_FILE = docker_compose/storages.yaml
APP_CONTAINER = miran2025/mir-cat-tg-bot
SERVICE_NAME = miran2025/mir-cat-tg-bot
IMAGE_NAME = miran2025/mir-cat-tg-bot

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

.PHONY: app-del
app-del:
	@${D} rmi ${IMAGE_NAME}

.PHONY: push
push:
	@${D} push ${IMAGE_NAME}

.PHONY: size
size:
	@${D} system df

.PHONY: cash
cash:
	@${D} system prune -f

.PHONY: app-build
app-build:
	@${D} build --build-arg UID=1000 --build-arg GID=1000 -t ${IMAGE_NAME} .

.PHONY: app-rebuild-push
app-rebuild-push:
	@$(MAKE) app-del
	@$(MAKE) cash
	@$(MAKE) app-build
	@$(MAKE) push
