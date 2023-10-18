
import json
import psycopg2
import helpers.log as myLog
from db import config
import resources.constant as constant

logger = myLog.logger(__name__)

def save(results):

    if len(results) == 0:
        logger.info('No data to save')
        return

    # Connexion à une base de données PostgreSQL
    with psycopg2.connect(
            database=config.get('database', 'DB_NAME'),
            user=config.get('database', 'DB_USER'),
            password=constant.DB_PASSWORD,
            host=config.get('database', 'DB_HOST'),
            port= config.get('database', 'DB_PORT')
        ) as con:
        cursor_obj = con.cursor()

        # Création de la table
        cursor_obj.execute("CREATE TABLE IF NOT EXISTS filtered_data (id SERIAL PRIMARY KEY, name VARCHAR(255), github_id VARCHAR(255), url VARCHAR(255), detected_file VARCHAR(255), raw_data TEXT)")    
        con.commit()

        for result in results:
            # Insertion des données
            cursor_obj.execute("INSERT INTO filtered_data (name, github_id, url, detected_file, raw_data) VALUES (%s, %s, %s, %s, %s)", (result['repository']['name'], result['repository']['id'], result['repository']['html_url'], result['path'], json.dumps(result) ))  
            con.commit()

    # Fermeture de la connexion
    cursor_obj.close()
    con.close()





    