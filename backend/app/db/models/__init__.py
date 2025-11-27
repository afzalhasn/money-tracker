"""Import model modules so they register on the project's declarative Base.

When Alembic's env.py imports `from app.db.base import Base`, make sure the
model modules are imported so `Base.metadata` contains the Table objects.
This file intentionally imports modules (not symbols) to execute their
definitions without creating circular import problems.
"""

# Import all model modules here so a single `import app.db.models` will
# execute them and register their classes on `Base`.
from . import (
	user,
	item,
	sale,
	purchase_batch,
	gst_ledger,
	document,
	investment,
	expense,
)

# Expose module names for convenience
__all__ = [
	"user",
	"item",
	"sale",
	"purchase_batch",
	"gst_ledger",
	"document",
	"investment",
	"expense",
]
