import asyncio, os, sys
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine

from alembic import context

# Adding project root to sys.path
sys.path.append(os.getcwd())

# 1. Importing base and models of project
from app.core.database import Base, DATABASE_URL
from app.models.models import User, ChatSession  # Importing models is necessary

# Alembic Config object
config = context.config

# Setting up logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 2. Set up target metadata so Alembic can track the tables
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode (Async)."""
    # Use the actual DATABASE_URL loaded from .env
    connectable = create_async_engine(
        DATABASE_URL,
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())