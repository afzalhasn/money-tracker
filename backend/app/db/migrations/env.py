import os
import logging
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

from app.core.config import settings
from app.db.base import Base  # Import all models through Base

config = context.config

# Ensure the alembic Config has the URL available under both keys some
# helpers expect: 'sqlalchemy.url' (common) and plain 'url' which
# sqlalchemy.engine.create.engine_from_config will pop when prefix is
# set to 'sqlalchemy.'. Setting both makes the env robust regardless of
# how sections/prefix are used below.
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
config.set_main_option("url", settings.DATABASE_URL)

# Interpret the config file for Python logging. If the alembic config
# does not contain the expected logging sections, fall back to a simple
# basic logging config so migrations don't crash on import.
if config.config_file_name and os.path.exists(config.config_file_name):
    try:
        fileConfig(config.config_file_name)
    except Exception:
        logging.basicConfig(level=logging.INFO)
else:
    logging.basicConfig(level=logging.INFO)

# Target metadata
target_metadata = Base.metadata

def run_migrations_offline():
    context.configure(
        url=settings.DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
