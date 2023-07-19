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
    logger.info('Searching for {} in Github files with language {}'.format(query, language))
    clean_results = []
    
    try:
        api_url = config.get('github', 'API_URL')

        url = '{}/search/code?q={}+language:{}+in:file'.format(api_url, query, language)

        raw_results = get_all_pages(url)

        clean_results = extract_repo_data(raw_results)


        logger.info('Found {} repositories for query {}'.format(len(clean_results), query))
        logger.info('Resulst: {}'.format(clean_results))

    except Exception as e:
        logger.error('Error while searching for {} in Github files with language {}'.format(query, language))
        logger.error(e)
        
    return clean_results
    # db.save(clean_results)


#---------------------------------------------------------------------------
#   Extract repo data
#---------------------------------------------------------------------------
#
# Function enabling to extract the data we want from the raw results
# returned by the github API.
#

# TODO:Implement this function
def extract_repo_data(raw_results):
    return raw_results