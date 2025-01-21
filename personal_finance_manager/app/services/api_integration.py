# app/services/api_integration.py

import requests

def fetch_transactions(api_key, account_id):
    url = f"https://api.bank.com/accounts/{account_id}/transactions"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None