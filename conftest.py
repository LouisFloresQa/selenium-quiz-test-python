import pytest
from utils.driver_factory import DriverFactory
from config import HEADLESS


@pytest.fixture(scope="function")
def driver():
    """
    Fixture pour créer et fournir un WebDriver pour les tests
    """
    # Initialiser le driver
    driver = DriverFactory.get_driver(headless=HEADLESS)
    
    # Céder le driver au test
    yield driver
    
    # Nettoyage: fermer le driver après le test
    driver.quit()
