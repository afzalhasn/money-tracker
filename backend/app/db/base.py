# backend/app/db/base.py
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import models so they are registered on the declarative Base.metadata.
# This keeps model imports centralized and ensures Alembic autogenerate
# can find tables when env.py imports `from app.db.base import Base`.
try:
	# import the package which in turn imports modules that define models
	import app.db.models  # noqa: F401
except Exception as _exc:
	# Avoid failing imports at module import time — Alembic may import this
	# file in environments where dependencies are missing. Log the
	# exception so it's easy to diagnose missing deps or import errors
	# when running migrations locally.
	import logging

	logging.getLogger(__name__).exception(
		"Failed to import app.db.models; models may not be registered on Base.metadata"
	)
