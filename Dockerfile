FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

ARG UID
ARG GID

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

COPY pyproject.toml uv.lock /app/

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-dev

COPY src/ /app/src/

RUN mkdir -p /app/logs \
    /app/excel && \
    groupadd -g $GID miran && \
    useradd -u $UID -g $GID -m miran && \
    chown -R miran:miran /app

USER miran

ENV PYTHONPATH=/app
ENV PATH="/app/.venv/bin/:$PATH"
