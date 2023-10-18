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
import resources.constant as constant

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
    page = int(config.get('github', 'INIT_PAGE'))
    results = []

    # Set the HTTP headers
    headers = {
            "Authorization": f"Bearer {constant.TOKEN}",
            "Accept": "application/vnd.github+json"
        }
    
    while True:
        if page > int(config.get('github', 'MAX_PAGE')):
            break
        try:
            r = requests.get(url=url, headers=headers, params={'page': page, 'per_page': int(config.get('github', 'NBR_PAGE_PER_REQUEST'))})

            logger.info('Getting page {} from github api'.format(page)) 
            
            if r.status_code == http.client.OK:
                results.append(r.json())
            else:
                break

            page += 1
            utils.delay_between_requests()

        except Exception as e:
            logger.error('Error while getting page {} from github api'.format(page))
            logger.error(e)
            break
    return results

        
def _get(url, withToken=False):
     # Set the HTTP headers
    headers = {
            "Accept": "application/vnd.github+json"
        }
    
    if(withToken):
        headers.add('Authorization', f"Bearer {constant.TOKEN}")
    
    try:
        r = requests.get(url=url, headers=headers)
        
        if r.status_code == http.client.OK:
            return r.json()
       
    except Exception as e:
        logger.error('Error while getting commit from github api {}'.format(url))
        logger.error(e)