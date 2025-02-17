from datetime import datetime

def get_date():
    """
    Renvoie la date du jour au format YYYY-MM-DD
    """

    return datetime.today().strftime("%Y-%m-%d")