from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class DriverFactory:
    """Factory pour créer une instance de WebDriver"""
    
    @staticmethod
    def get_driver(browser_name="chrome", headless=False):
        """
        Obtenir une instance de WebDriver
        :param browser_name: Nom du navigateur ('chrome' par défaut)
        :param headless: Exécuter en mode headless (sans interface graphique)
        :return: Instance de WebDriver
        """
        if browser_name.lower() == "chrome":
            options = Options()
            
            # Configuration des options Chrome
            options.add_argument("--start-maximized")
            if headless:
                options.add_argument("--headless")
            
            # Configuration pour éviter les problèmes de détection de bot
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)
            
            # Créer le driver avec webdriver-manager pour la gestion automatique des versions
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=options
            )
            
            # Effacer les traces d'automatisation
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            return driver
        else:
            raise ValueError(f"Navigateur non supporté: {browser_name}")
