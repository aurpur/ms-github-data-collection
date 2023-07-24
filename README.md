# Microservice Github Data Collection
Utiliser la librairie flask https://flask.palletsprojects.com/en/2.3.x/quickstart/

https://python.developpez.com/tutoriel/intro-flask-python3/

Gestion des properties : https://www.digitalocean.com/community/tutorials/python-read-properties-file


TODO :

Generer automatiquement la Query
BD en ligne
Github action
   Exécution chaque heure ?

DB to CSV

from DB get list of repositories ?

Get repository meta data (starts number, commit number, last commit date, contributors numbers, ...) (voir Amin paper)


Web app to count numbre of registery in db



Add variable d'environnement sur mac

nano $HOME/.zshrc
** export YOUR_VARIABLE=your_value
source $HOME/.zshrc


** Terminal 
>>echo $DB_PASSWORD
echo $GITHUB_TOKEN


** In source code (constant.py)
>> TOKEN = os.getenv('GITHUB_TOKEN')
print(TOKEN)
