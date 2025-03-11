from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.toolbox_page import ToolboxPage



class HomePage(BasePage):
    """Page d'accueil du site hightest.nc"""
    
    # Locators
    TOOLBOX_LINK = (By.CSS_SELECTOR, "li[id='menu-item-33']")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def load(self, url):
        """Charger la page d'accueil"""
        self.driver.get(url)
        return self
        
    def click_toolbox(self):
        """Cliquer sur le lien Toolbox"""
        self.click_element(self.TOOLBOX_LINK)

        return ToolboxPage(self.driver)