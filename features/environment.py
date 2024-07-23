import logging
import psycopg2
from browser_actions import CdiscountBot

# Configurer le logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def before_all(context):
    try:
        logging.info("Initialisation du WebDriver")
        context.browser = CdiscountBot()
        context.conn = psycopg2.connect("dbname=mydb user=myuser password=mypassword")  
        context.cursor = context.conn.cursor()
        logging.info("WebDriver et base de données initialisés avec succès")
    except Exception as e:
        logging.error(f"Erreur lors de l'initialisation du WebDriver ou de la base de données: {e}")

def after_all(context):
    try:
        context.browser.quit()
        context.cursor.close()
        context.conn.close()
        logging.info("WebDriver et base de données fermés avec succès")
    except Exception as e:
        logging.error(f"Erreur lors de la fermeture du WebDriver ou de la base de données: {e}")