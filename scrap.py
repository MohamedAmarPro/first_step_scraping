# Importation des bibliothèques nécessaires
import requests
from bs4 import BeautifulSoup

# Définition de l'agent utilisateur (user-agent) pour les requêtes HTTP
navigator = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'

# URL de la page web à scraper
url = "http://www.chucknorrisfacts.fr/facts/top/1"

# Faire une requête HTTP GET pour obtenir le contenu de la page
html = requests.get(url, headers={'User-Agent': navigator})

# Créer un objet BeautifulSoup pour analyser le HTML de la page
soup = BeautifulSoup(html.text, 'html.parser')

# Extraire les éléments HTML contenant les blagues (balises <p>) et les notes (balises <span>)
blagues = soup.findAll('p')
blague8 = blagues[7].get_text()

notes = soup.findAll('span')
note8 = notes[7].get_text()

# Initialiser un dictionnaire pour stocker les blagues et les notes
blagues_et_notes = {}

# Boucle pour extraire les 20 premières blagues et notes
for i in range(21):
    # Extraire le texte de la blague à l'indice i
    blague = blagues[i].get_text()

    # Extraire le texte de la note correspondante à l'indice i
    note = notes[i].get_text()

    # Ajouter la paire blague-note au dictionnaire
    blagues_et_notes[blague] = note

# Afficher le dictionnaire complet contenant les blagues et les notes
print(blagues_et_notes)

