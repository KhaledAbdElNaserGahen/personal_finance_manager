# app/models/database.py

import sqlite3

def init_db():
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount FLOAT,
            category TEXT,
            description TEXT,
            date TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            category TEXT PRIMARY KEY,
            budget_amount FLOAT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            goal_name TEXT,
            target_amount FLOAT,
            target_date TEXT,
            progress FLOAT
        )
    ''')
    conn.commit()
    conn.close()

def get_transactions():
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    transactions = cursor.fetchall()
    conn.close()
    return transactions

def add_transaction(amount, category, description, date):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    ''', (amount, category, description, date))
    conn.commit()
    conn.close()

def set_budget(category, budget_amount):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO budgets (category, budget_amount)
        VALUES (?, ?)
        ON CONFLICT(category) DO UPDATE SET budget_amount=excluded.budget_amount
    ''', (category, budget_amount))
    conn.commit()
    conn.close()

def get_budgets():
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM budgets')
    budgets = cursor.fetchall()
    conn.close()
    return budgets

def get_total_spent():
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT category, SUM(amount) as total_spent FROM transactions GROUP BY category
    ''')
    spent = {category: total for category, total in cursor.fetchall()}
    conn.close()
    return spent

def set_goal(goal_name, target_amount, target_date):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO goals (goal_name, target_amount, target_date, progress)
        VALUES (?, ?, ?, ?)
    ''', (goal_name, target_amount, target_date, 0))
    conn.commit()
    conn.close()

def get_goals():
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM goals')
    goals = cursor.fetchall()
    conn.close()
    return goals

def update_goal_progress(goal_name, progress):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE goals SET progress = ?
        WHERE goal_name = ?
    ''', (progress, goal_name))
    conn.commit()
    conn.close