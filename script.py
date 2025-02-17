import requests
import os
import time
from dotenv import load_dotenv
from save_to_excel import save_to_excel
from get_date import get_date

load_dotenv()  # Charge les variables d'environnement depuis .env


def fetch_bodacc_data():
    start_time = time.time()
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

    try:
        while True:
            response = requests.get(url=url, params=params)
            data = response.json()

            if not data.get("results"):
                break

            records.extend(data["results"])
            params["offset"] += 100

        print(f"Nombre total de nouvelles procédures : {len(records)}")
        print(records)

        save_to_excel(records)

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Temps d'exécution : {execution_time}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion API: {e}")
    except ValueError as e:
        print(f"❌ Erreur lors du traitement de la réponse JSON: {e}")
    except Exception as e:
        print(f"❌ Une erreur inattendue est survenue dans fetch_bodacc_data: {e}")

fetch_bodacc_data()