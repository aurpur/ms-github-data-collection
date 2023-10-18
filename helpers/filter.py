from api.rest import _get
import helpers.log as myLog

logger = myLog.logger(__name__)

def filter_repositories(data):

    results = []

    #TODO: 
   
    logger.info('Filtering data...')
    
    for item in data:
      
    # Filtering data by number of commit > 100
    # Filtering data with last commit date > 5 years 
    # Filtering data by number of stars > 100  
    # Filtering data by number of contributors > 5 

        commitsUrl = item['repository']['commits_url'].replace('{/sha}', '') 
        starUrl = item['repository']['stargazers_url']
        contributorsUrl = item['repository']['contributors_url']

        
        commits = _get(commitsUrl)
        commitLength = 0


        if commits is not None:
            commitLength = len(commits)

        if commitLength >= 15:
            logger.info('\n\nFound {} commits in repository {}'.format(commitLength, item['repository']['full_name']))
            lastCommit = commits[0]['commit']['author']['date']
            

        

            if lastCommit < '2018-01-01T00:00:00Z':
                logger.info('\n\nLast commit date is {} for repository {}'.format(lastCommit, item['repository']['full_name']))

                stars = _get(starUrl)
                contributors = _get(contributorsUrl)

                
                starLength = len(stars)
                contributorLength = len(contributors)

                if starLength >= 5 and contributorLength >= 2:
                    results.append(item)
                    logger.info('\n\nFound {} stars and {} contributors in repository {}'.format(starLength, contributorLength, item['repository']['full_name']))
            

    if len(results) == 0:
        logger.info('\n\n==++==> No repositories found after filtering')
    

    return results