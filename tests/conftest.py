import pytest
from src.start import create_app

@pytest.fixture()
def app():
    
    app = create_app()

    yield app

    # teardown here

@pytest.fixture()
def client(app):
    return app.test_client()
