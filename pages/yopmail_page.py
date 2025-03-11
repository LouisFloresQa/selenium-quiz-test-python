from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time


class YopmailPage(BasePage):
    """Page Yopmail pour vérifier les emails"""

    # Locators
    EMAIL_INPUT = (By.ID, "login")
    CHECK_INBOX_BUTTON = (By.CSS_SELECTOR, "#refreshbut > button > i")  # Bouton de rafraîchissement
    IFRAME_INBOX = (By.ID, "ifinbox")  # Iframe de la boîte de réception
    IFRAME_MAIL = (By.ID, "ifmail")  # Iframe du contenu de l'e-mail
    MOST_RECENT_EMAIL = (By.CSS_SELECTOR, "div.m:first-child")  # Premier e-mail dans la liste
    EMAIL_CONTENT = (By.CSS_SELECTOR, "#mail > div > div")  # Contenu de l'e-mail

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        """Charger le site Yopmail"""
        self.driver.get("https://yopmail.com")
        return self

    def check_inbox(self, email):
        """Consulter la boîte de réception"""
        # Entrer l'e-mail
        self.input_text(self.EMAIL_INPUT, email)
        print(f"Email entered: {email}")

        # Attendre que le bouton de rafraîchissement soit cliquable
        try:
            refresh_button = self.wait.until(EC.element_to_be_clickable(self.CHECK_INBOX_BUTTON))
            print("Refresh button is clickable.")
        except Exception as e:
            print(f"Failed to find refresh button: {str(e)}")
            self.driver.save_screenshot("refresh_button_error.png")
            raise

        # Cliquer sur le bouton de rafraîchissement
        refresh_button.click()
        print("Refresh button clicked.")

        # Attendre que la boîte de réception se rafraîchisse
        time.sleep(2)
        return self

    def open_most_recent_email(self, search_text):
        """Ouvrir l'email le plus récent contenant le texte recherché"""
        # Basculer dans l'iframe de la boîte de réception
        self.switch_to_frame(self.IFRAME_INBOX)

        # Trouver tous les e-mails
        emails = self.driver.find_elements(By.CSS_SELECTOR, "div.m")

        # Parcourir les e-mails pour trouver celui qui contient le texte recherché
        for email in emails:
            email_text = email.text
            if search_text in email_text:
                # Cliquer sur l'e-mail correspondant
                email.click()
                print(f"Email containing '{search_text}' found and opened.")
                break

        # Revenir au contenu principal
        self.switch_to_default_content()
        return self

    def get_email_content(self):
        """Lire le contenu de l'email"""
        # Basculer dans l'iframe du mail
        self.switch_to_frame(self.IFRAME_MAIL)

        # Attendre que le contenu de l'e-mail soit présent
        try:
            content_element = self.wait.until(EC.presence_of_element_located(self.EMAIL_CONTENT))
            print("Email content element found.")
        except Exception as e:
            print(f"Failed to find email content: {str(e)}")
            self.driver.save_screenshot("email_content_error.png")
            raise

        # Récupérer le texte du contenu de l'e-mail
        content = content_element.text
        print("Email content retrieved successfully.")

        # Revenir au contenu principal
        self.switch_to_default_content()
        return content

    def verify_score_in_email(self, search_text):
        """Vérifier si l'email contient le texte recherché"""
        email_content = self.get_email_content()
        return search_text in email_content