import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from save_to_excel import save_to_excel
from get_date import get_date

load_dotenv()  # Charge les variables d'environnement depuis .env

url = os.getenv("API_BODACC_BASE_URL")
date = get_date()
records = []
params = {
    "offset": 0,
    "limit": 100,
    "refine": [
        'familleavis_lib:"Procédures collectives"',
        f'dateparution:{date}'
    ]
}

def fetch_bodacc_data():
    while True:
        response = requests.get(url=url, params=params)
        data = response.json()

        if not data.get("results"):
            break

        records.extend(data["results"])
        params["offset"] += 100

    print(f"Nombre total de nouvelles procédures : {len(records)}")
    print(records)

    save_to_excel(records, date=date)

fetch_bodacc_data()