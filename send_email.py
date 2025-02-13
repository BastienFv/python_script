import smtplib
import os
from email.message import EmailMessage

def send_email(filename, date):
    sender_email = os.getenv("EMAIL_FROM_ADRESS")
    sender_password = os.getenv("EMAIL_FROM_PASSWORD")
    receiver_email = os.getenv("EMAIL_TO_ADRESS")
    subject = "Fichier Excel Bodacc"
    body = f"Bonnnnnnnsoirrrr Paulllll HIHIHIHIHI,\n\n. Voici le fichier Excel contenant les enregistrements du BODACC du 2025-02-04./n/n Ouiiii elle a des biscuitssssss"

    # Créer l'email
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    # Ajouter le fichier en pièce jointe
    with open(filename, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(filename)

    msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    # Se connecter au serveur SMTP et envoyer l'email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Remplace par ton serveur SMTP si besoin
            server.starttls()  # Sécuriser la connexion
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        print(f"✅ Email envoyé à {receiver_email} avec la pièce jointe {filename} !")
    
    except Exception as e:
        print(f"❌ Erreur lors de l'envoi de l'email : {e}")