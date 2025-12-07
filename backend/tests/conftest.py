import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.api.v1.routes import items, purchases, sales
from app.db.base import Base
from app.main import create_app

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


def override_test_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="session", autouse=True)
def initialize_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(autouse=True)
def cleanup_tables():
    yield
    with engine.begin() as conn:
        for table in reversed(Base.metadata.sorted_tables):
            conn.execute(table.delete())


@pytest.fixture(scope="module")
def test_client():
    """Create a FastAPI TestClient with dependencies overridden for tests."""
    app = create_app()
    app.dependency_overrides[items.get_db] = override_test_db
    app.dependency_overrides[purchases.get_db] = override_test_db
    app.dependency_overrides[sales.get_db] = override_test_db

    with TestClient(app) as client:
        yield client
