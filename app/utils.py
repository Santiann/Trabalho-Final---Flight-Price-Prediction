import pandas as pd

REQUIRED_COLUMNS = ['airline', 'flight', 'source_city', 'departure_time', 'stops', 'arrival_time', 'destination_city', 'class', 'duration', 'days_left', 'price']  # Altere conforme necessário

def validate_csv(filepath):
    try:
        df = pd.read_csv(filepath)
        return all(col in df.columns for col in REQUIRED_COLUMNS)
    except Exception as e:
        print(f"Erro ao validar CSV: {e}")
        return False
