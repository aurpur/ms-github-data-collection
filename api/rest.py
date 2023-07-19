# This file contains the functions to get data from the github REST api

#---------------------------------------------------------------------------
#   Imports
#---------------------------------------------------------------------------
#
# Here we import the modules we need for the script.
# The modules are located in the same folder as this script.
#

import requests
import http.client
from api import config
import helpers.log as myLog
import helpers.utils as utils

#---------------------------------------------------------------------------
#   Logging
#---------------------------------------------------------------------------
#
# Here we create a logger for this script.
# The logger will be named after the script's name.
#

logger = myLog.logger(__name__)

#---------------------------------------------------------------------------
#   Get all pages
#---------------------------------------------------------------------------
#
# Function enabling to get all pages from github api
#

def get_all_pages(url):

   # Get all pages from github api
    page = config.get('github', 'INIT_PAGE')
    results = []

    # Set the HTTP headers
    headers = {
            "Authorization": f"Bearer {config.get('github', 'TOKEN')}",
            "Accept": "application/vnd.github+json"
        }
    
    while True:
        if page > config.get('github', 'MAX_PAGE'):
            break
        try:
            r = requests.get(url=url, headers=headers, params={'page': page, 'per_page': config.get('github', 'NBR_PAGE_PER_REQUEST')})

            if r.status_code == http.client.OK:
                results.append(r.json())
                page += config.get('default', 'INCREMENT')
            else:
                break

            utils.delay_between_requests()

        except Exception as e:
            logger.error('Error while getting page {} from github api'.format(page))
            logger.error(e)
            break
    return results

        
