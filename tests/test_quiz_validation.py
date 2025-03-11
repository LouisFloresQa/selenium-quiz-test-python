import pytest
from pages.home_page import HomePage
from utils.quiz_answers import CORRECT_ANSWERS
from config import BASE_URL, TEST_EMAIL
from selenium.webdriver.support import expected_conditions as EC
import time


class TestQuizValidation:
    """Test de validation du quiz avec vérification d'e-mail"""

    def test_quiz_completion_email(self, driver):
        """
        Test vérifiant qu'un quiz correctement rempli génère un e-mail
        indiquant 100% de réussite
        """
        # 1. Accéder à la page d'accueil
        home_page = HomePage(driver)
        home_page.load(BASE_URL)

        # 2. Naviguer vers la page Toolbox
        toolbox_page = home_page.click_toolbox()

        # 3. Cliquer sur le lien du quiz ISTQB Agile
        quiz_page = toolbox_page.click_quiz_istqb_agile()

        # Débogage : Afficher le titre de la page pour confirmer que nous sommes sur la bonne page
        print(f"Titre de la page du quiz : {driver.title}")
        driver.save_screenshot("quiz_page.png")

        # 4. Compléter le quiz avec les bonnes réponses
        quiz_page.complete_quiz(CORRECT_ANSWERS)

        # 5. Soumettre le quiz
        result_page = quiz_page.submit_quiz()

        # 6. Entrer l'adresse email et soumettre
        result_page.enter_email(TEST_EMAIL)
        result_page.submit_email()

        # Attendre quelques secondes pour que l'email soit envoyé
        time.sleep(5)

        # 7. Accéder à Yopmail et vérifier le contenu de l'email
        from pages.yopmail_page import YopmailPage
        yopmail_page = YopmailPage(driver)
        yopmail_page.load()

        # Vérifier la boîte de réception et rafraîchir
        yopmail_page.check_inbox(TEST_EMAIL)

        # Ouvrir l'e-mail le plus récent contenant "100"
        yopmail_page.open_most_recent_email("100")

        # 8. Vérifier que l'email contient "100%"
        assert yopmail_page.verify_score_in_email("100"), "L'email ne mentionne pas 100 % de réussite"

        # 9. Fermer la nouvelle fenêtre ou onglet et revenir à la fenêtre principale
        driver.close()  # Ferme la fenêtre actuelle (le quiz)
        driver.switch_to.window(driver.window_handles[0])  # Revenir à la fenêtre principale