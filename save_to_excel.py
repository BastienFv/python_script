import pandas as pd
from get_date import get_date
from send_email import send_email


def save_to_excel(records):
    """
    Génére un fichier excel
    """
    today = get_date()
    filename = f"bodacc_{today}.xlsx"

    if not records:
        print("Pas de nouveaux enregistrements aujourd'hui.")
        return
    
    try:
        # Convertir en DataFrame pandas
        df = pd.DataFrame(records)

        # Sauvegarder en fichier Excel
        df.to_excel(filename, index=False)

        print(f"✅ Le fichier Excel a bien été généré.")

        send_email(filename=filename, date=today)
    
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde du fichier Excel: {e}")