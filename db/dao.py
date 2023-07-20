
def save(results):

    for result in results:
        print('Name: {}'.format(result['name']))
        print('Path: {}'.format(result['path']))
        print('URL: {}'.format(result['url']))
    print('Saving results in database')

    