from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.result_page import ResultPage  # Assurez-vous que ResultPage est importé


class QuizPage(BasePage):
    """Page du quiz ISTQB Agile"""

    # Locators
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")  # Sélecteur CSS pour le bouton de soumission

    def __init__(self, driver):
        super().__init__(driver)

    def answer_question(self, question_number, answer_value):
        """
        Répondre à une question du quiz
        :param question_number: Le numéro de la question (0, 1, 2, etc.)
        :param answer_value: La valeur de la réponse (1, 2, 3, 4)
        """
        locator = (By.CSS_SELECTOR, f"input[name='{question_number}'][type='radio'][value='{answer_value}']")
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        import time
        time.sleep(0.5)
        self.click_element(locator)
        return self

    def complete_quiz(self, answers_dict):
        """
        Compléter le quiz en utilisant un dictionnaire de réponses
        :param answers_dict: Dictionnaire {numéro_question: valeur_réponse}
        """
        print("Début du remplissage du quiz...")
        for question_number, answer_value in answers_dict.items():
            try:
                print(f"Tentative de réponse à la question {question_number}, réponse {answer_value}")
                self.answer_question(question_number, answer_value)
                print(f"Réponse à la question {question_number} réussie")
            except Exception as e:
                print(f"Erreur lors de la réponse à la question {question_number}: {str(e)}")
                self.driver.save_screenshot(f"error_q{question_number}.png")
                raise
        print("Quiz complété avec succès")
        return self

    def submit_quiz(self):
        """Soumettre le quiz en cliquant sur 'Terminé !'"""
        try:
            # Attendre que le bouton de soumission soit visible
            submit_button = self.wait.until(EC.visibility_of_element_located(self.SUBMIT_BUTTON))
            print(f"Found submit button with value: {submit_button.get_attribute('value')}")

            # Faire défiler jusqu'au bouton pour s'assurer qu'il est visible
            self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

            # Cliquer sur le bouton de soumission
            submit_button.click()
            print("Submit button clicked successfully.")
        except Exception as e:
            # En cas d'échec, prendre une capture d'écran et lever une exception
            print(f"Failed to find or click submit button: {str(e)}")
            self.driver.save_screenshot("submit_button_error.png")
            raise Exception("Failed to find or click the submit button with CSS selector #submit.")

        # Retourner la page de résultat
        return ResultPage(self.driver)