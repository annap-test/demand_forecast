# app/config.py

DATA_PATH = "data/"
your_file_id_for_stores_csv = '15Gvqx2-zn9XWaaaNKD8Tg1fGNh5axbHM'
your_file_id_for_items_csv = '1nclME03wt2SVt-CqXd7V42RzW1W8S2GM'
your_file_id_for_transactions_csv = '1-3Ga1UR_hQJ-PB7HPGd7Jcc7CxLYGoW0'
your_file_id_for_oil_csv = '1fFrX3rQW9XkGQn9RuZCYxNsK6GNlssOD'
your_file_id_for_holidays_csv = '1vifHhm2qzcPV3G0UpDFYYjrvKq41JOxM'
your_file_id_for_train_csv = '1-1uMbq0JlRO8ERO6jZHX2376UcHVqWOE'

# Google Drive links for each file (replace with actual file IDs)
GOOGLE_DRIVE_LINKS = {
    "stores": f"https://drive.google.com/uc?id={your_file_id_for_stores_csv}",
    "items": f"https://drive.google.com/uc?id={your_file_id_for_items_csv}",
    "transactions": f"https://drive.google.com/uc?id={your_file_id_for_transactions_csv}",
    "oil": f"https://drive.google.com/uc?id={your_file_id_for_oil_csv}",
    "holidays_events": f"https://drive.google.com/uc?id={your_file_id_for_holidays_csv}",
    "train": f"https://drive.google.com/uc?id={your_file_id_for_train_csv}"
}

MODEL_PATH = 'model/'
your_file_id_for_xgboost_model_xgb = "1hd-TQvzEOnh-WZvLsaxsnCguhku4spxq"  # Replace with the actual file ID for model.xgb from MLFlow aritifacts
GOOGLE_DRIVE_LINKS_MODELS = {
    "xgboost_model": f"https://drive.google.com/uc?id={your_file_id_for_xgboost_model_xgb}"
}