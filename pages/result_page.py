from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ResultPage(BasePage):
    """Page de résultat du quiz"""
    
    # Locators
    EMAIL_INPUT = (By.ID, "email")
    SUBMIT_MAIL_BUTTON = (By.CSS_SELECTOR, "input#submitMail[name='submitMail'][type='submit'][value='OK']")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def enter_email(self, email):
        """Saisir l'adresse email"""
        self.input_text(self.EMAIL_INPUT, email)
        return self
    
    def submit_email(self):
        """Soumettre le formulaire email en cliquant sur 'OK'"""
        self.click_element(self.SUBMIT_MAIL_BUTTON)
        return self
