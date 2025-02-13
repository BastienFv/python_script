import pandas as pd
from datetime import datetime
from send_email import send_email

today = datetime.today().strftime("%Y-%m-%d")  # Format YYYY-MM-DD
filename = f"bodacc_{today}.xlsx"

def save_to_excel(records):
    if not records:
        print("Pas de nouveaux enregistrements aujourd'hui.")
        return
    
    # Convertir en DataFrame pandas
    df = pd.DataFrame(records)

    # Sauvegarder en fichier Excel
    df.to_excel(filename, index=False)

    print(f"✅ Fichier Excel généré avec {len(records)} enregistrements : {filename}")

    send_email(filename=filename, date=today)