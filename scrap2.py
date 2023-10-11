import requests
from bs4 import BeautifulSoup
import pandas as pd

# Définition de l'agent utilisateur (user-agent) pour les requêtes HTTP
navigator = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'

# Initialisation d'une liste pour stocker les données de chaque page
blagues_et_notes_list = []

for i in range(1, 6): 
    # URL de la page web à scraper
    url = 'http://www.chucknorrisfacts.fr/facts/top/' + str(i)

    # Faire une requête HTTP GET pour obtenir le contenu de la page
    html = requests.get(url, headers={'User-Agent': navigator})

    # Créer un objet BeautifulSoup pour analyser le HTML de la page
    soup = BeautifulSoup(html.text, 'html.parser')

    # Extraire les éléments HTML contenant les blagues (balises <p>) et les notes (balises <span>)
    blagues = soup.findAll('p')
    notes = soup.findAll('span')

    # Boucle pour extraire les blagues et les notes de chaque page
    for j in range(20):
        blague = blagues[j].get_text()
        note = notes[j].get_text()
        blagues_et_notes_list.append([blague, note])

# Créer un DataFrame à partir de la liste de blagues et notes
df = pd.DataFrame(blagues_et_notes_list, columns=["blague", "note"])

# Afficher le DataFrame
print(df)
