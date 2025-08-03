from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

# Chemin vers le fichier CSV dans le même dossier que app.py
csv_path = os.path.join(os.path.dirname(__file__), 'codes.csv')

@app.route('/')
def index():
    tickets = []
    # On ouvre le CSV et on lit ligne par ligne avec DictReader pour avoir un dict par ligne
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tickets.append(row)
    # On envoie la liste des tickets au template test.html
    return render_template('index.html', tickets=tickets)

if __name__ == '__main__':
    app.run(debug=True)
