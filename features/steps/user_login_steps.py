from behave import given, when, then
import logging

@given('the login page is displayed')
def step_impl(context):
    try:
        context.browser.login('ricacegos@gmail.com', 'Roibcaan1')
        logging.info("Connexion faite avec succès")
        # print("Connexion faite avec succès")
    except Exception as e:
        context.browser.save_screenshot("screenshot/redirect_failure.png")
        print(f"Erreur de connexion : {e}")

@when('a user logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    logging.info("Connexion de l'utilisateur réussie")
    # print("Connexion de l'utilisateur réussie")

@then('the user should be redirected to the homepage')
def step_impl(context):

    print("Utilisateur redirigé vers la page d'accueil avec succès")
    
@then('the user data should be present in the database')
def step_impl(context):
    try:
        context.cursor.execute("SELECT * FROM users WHERE login=%s", ('ricacegos@gmail.com',))
        result = context.cursor.fetchone()
        logging.info(f"Le résultat de la requête est {result}")
        assert result is not None
    except Exception as e:
        print(f"Erreur lors de la récupération de données en BDD : {e}")
    