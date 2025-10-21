# Django Cucine
Applicazione web per catalogo e vendita cucine con pannello amministrativo

## 🚀 Demo
[Visualizza l'applicazione live](https://nicmarp4.pythonanywhere.com/)

## 🛠️ Tecnologie
- Django
- Python 
- HTML/CSS
- PythonAnywhere (deploy)

## 📋 Prerequisiti
- Python 3.8+
- pip



## 📄 Licenza
MIT License


### ⚡ Installazione locale
#### segui questi comandi

#### installa ambiente virtuale


python -m venv venv    

#### attivalo con

.\venv\Scripts\activate


#### entra nella cartella del progetto

cd .\djangocucine-main\


#### installa le dipendenze

pip install -r requirements.txt 



#### il progetto è già popolato tramite il file  

djangocucine-main\prodotti\management\commands\popola_database.py


#### avviabile col comando

python manage.py popola_database


#### il progetto si può resettare tramite il file

djangocucine-main\prodotti\management\commands\rimuovi_demo.py

#### con il comando

python manage.py rimuovi_demo
