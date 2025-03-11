from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ToolboxPage(BasePage):
    """Page Toolbox du site hightest.nc"""

    # Locators
    QUIZ_ISTQB_AGILE_LINK = (By.CSS_SELECTOR, "a[href='https://hightest.nc/ressources/test-istqb-agile.php']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_quiz_istqb_agile(self):
        """Cliquer sur le lien vers le quiz ISTQB Agile et basculer vers la nouvelle fenêtre ou onglet"""

        # Store current URL and window handle
        current_url = self.driver.current_url
        main_window_handle = self.driver.current_window_handle
        print(f"Current URL before clicking quiz link: {current_url}")

        # Trouver et cliquer sur le lien du quiz
        try:
            # Attendre que l'élément soit présent dans le DOM
            element = self.wait.until(EC.presence_of_element_located(self.QUIZ_ISTQB_AGILE_LINK))
            print(f"Found quiz link with href: {element.get_attribute('href')}")

            # Faire défiler la page jusqu'à ce que l'élément soit visible
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            # Attendre que l'élément soit cliquable
            element = self.wait.until(EC.element_to_be_clickable(self.QUIZ_ISTQB_AGILE_LINK))
            print("Quiz link is clickable.")

            # Cliquer sur l'élément
            element.click()
            print("Quiz link clicked.")
        except Exception as e:
            print(f"Failed to find or click quiz link: {str(e)}")
            self.driver.save_screenshot("quiz_link_error.png")
            raise

        # Attendre que la nouvelle fenêtre ou onglet s'ouvre
        WebDriverWait(self.driver, 20).until(lambda driver: len(driver.window_handles) > 1)

        # Basculer vers la nouvelle fenêtre ou onglet
        new_window_handle = [handle for handle in self.driver.window_handles if handle != main_window_handle][0]
        self.driver.switch_to.window(new_window_handle)

        # Attendre que la nouvelle page soit chargée
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.current_url != current_url
        )

        # Vérifier que l'URL est correcte
        new_url = self.driver.current_url
        print(f"New URL after clicking quiz link: {new_url}")

        if "test-istqb-agile.php" not in new_url:
            print("WARNING: Navigation may have failed - URL doesn't contain expected pattern")
            self.driver.save_screenshot("navigation_failure.png")

        from pages.quiz_page import QuizPage
        return QuizPage(self.driver)