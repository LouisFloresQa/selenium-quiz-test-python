# Test Automatisé de Quiz avec Selenium

Ce projet implémente un test automatisé utilisant Selenium WebDriver pour vérifier qu'un quiz correctement rempli sur le site hightest.nc génère un email confirmant un score de 100%.

## Architecture

Le projet suit le design pattern Page Object Model (POM) pour améliorer la maintenabilité et la lisibilité du code.

```
selenium-quiz-test/
│
├── .gitignore
├── requirements.txt
├── README.md
├── conftest.py
├── config.py
│
├── tests/
│   ├── __init__.py
│   └── test_quiz_validation.py
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── toolbox_page.py
│   ├── quiz_page.py
│   ├── result_page.py
│   └── yopmail_page.py
│
└── utils/
    ├── __init__.py
    ├── driver_factory.py
    └── quiz_answers.py
```

## Prérequis

- Python 3.8+
- Google Chrome
- Connexion Internet

## Installation

1. Cloner le dépôt :
```
git clone https://github.com/LouisFloresQa/selenium-quiz-test-python.git
cd selenium-quiz-test
```

2. Créer et activer un environnement virtuel :
```
python3 -m venv flfhighenv
```

3. Installer les dépendances :
```
pip install -r requirements.txt
```

## Configuration

Les paramètres de configuration se trouvent dans le fichier `config.py` :
- URLs des sites
- Adresse email pour le test
- Timeouts
- Options d'exécution (headless, etc.)

## Exécution des Tests

Pour exécuter le test :
```
./flfhighenv/bin/python -m pytest tests/test_quiz_validation.py -v```
```

Pour générer un rapport HTML :
```
pytest tests/test_quiz_validation.py -v --html=report.html
```

## Description du Scénario de Test

1. Accéder à https://hightest.nc/
2. Cliquer sur "Toolbox"
3. Cliquer sur le lien vers le quiz ISTQB Agile
4. Répondre correctement à toutes les questions du quiz
5. Soumettre le quiz
6. Entrer l'adresse email hightestflores@yopmail.com
7. Valider le formulaire
8. Vérifier dans la boîte mail Yopmail que l'email reçu indique 100% de bonnes réponses

## Notes Importantes

- Le fichier `utils/quiz_answers.py` contient des réponses hypothétiques. Il faut remplacer ces valeurs par les véritables bonnes réponses au quiz.
- Le test utilise ChromeDriver, qui sera automatiquement téléchargé grâce à webdriver-manager.
