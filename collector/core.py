# This file contains the core functions of the collector from repositories like Github.

#---------------------------------------------------------------------------
#   Imports
#---------------------------------------------------------------------------
#
# Here we import the modules we need for the script.
# The modules are located in the same folder as this script.
#

import helpers.log as myLog
from collector import config
from api.rest import get_all_pages
import db.dao as db
import random

#---------------------------------------------------------------------------
#   Logging
#---------------------------------------------------------------------------
#
# Here we create a logger for this script.
# The logger will be named after the script's name.
#

logger = myLog.logger(__name__)

#---------------------------------------------------------------------------
#   Search in code
#---------------------------------------------------------------------------
#
# Function enabling to search for a query in github files with a specific
# language (default is python) and save a list of repositories containing
# the query in their files.
#

def search_in_code(query, language='python'):
    """Search query in github files with language in parameter"""
    clean_results = []
    
    try:
        api_url = config.get('github', 'API_URL')

        url = '{}/search/code?q={}+language:{}'.format(api_url, query, language)

        raw_results = get_all_pages(url)

        clean_results = extract_repo_data(raw_results)

        logger.info('\n\nFound \033[1m{}\033[0m repositories \nQuery q=\033[1m{}\033[0m+language:\033[1m{}\033[0m\n'.format(len(clean_results), query, language))
   
    except Exception as e:
        logger.error('Error while searching for {} in Github files with language {}'.format(query, language))
        logger.error(e)
        
    db.save(clean_results)
    return clean_results
    


#---------------------------------------------------------------------------
#   Extract repo data
#---------------------------------------------------------------------------
#
# Function enabling to extract the data we want from the raw results
# returned by the github API.
#

def extract_repo_data(raw_results):
    result = []

    for dictOject in raw_results:
        for item in dictOject['items']:
            result.append(item)

    return result

#---------------------------------------------------------------------------
#   Generate query
#---------------------------------------------------------------------------
#
# Function enabling to generate a query for the Github API.
#

def generate_query(isAll=False):

    queries = ['keras.layers',
    'keras.layers.convolutional',
    'AveragePooling2D',
    'MaxPooling2D',
    'tensorflow.keras.layers',
    'Conv2D',
    'Convolution2D',
    'BatchNormalization']

    if(isAll):
        return queries
    
    return random.choice(queries)