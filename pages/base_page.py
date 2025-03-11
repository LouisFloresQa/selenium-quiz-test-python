from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Page de base qui sera héritée par toutes les classes de page"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Trouver un élément avec attente explicite"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_clickable_element(self, locator):
        """Trouver un élément cliquable avec attente explicite"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        """Cliquer sur un élément avec attente explicite"""
        element = self.find_clickable_element(locator)
        element.click()
        return element

    def input_text(self, locator, text):
        """Saisir du texte dans un élément"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return element

    def is_element_present(self, locator, timeout=10):
        """Vérifier si un élément est présent"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_text(self, locator):
        """Obtenir le texte d'un élément"""
        element = self.find_element(locator)
        return element.text
    
    def switch_to_frame(self, locator):
        """Basculer vers un iframe"""
        iframe = self.find_element(locator)
        self.driver.switch_to.frame(iframe)
    
    def switch_to_default_content(self):
        """Revenir au contenu principal depuis un iframe"""
        self.driver.switch_to.default_content()
