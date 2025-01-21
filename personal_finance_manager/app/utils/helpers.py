# app/utils/helpers.py

import sqlite3

def get_db_connection():
    conn = sqlite3.connect('finance_manager.db')
    return conn