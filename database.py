import sqlite3
from datetime import datetime
import json

class ToolNetDB:
    def __init__(self, db_file="toolnet.db"):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target TEXT,
                date TEXT,
                scan_type TEXT,
                open_ports INTEGER,
                ml_risk TEXT,
                results TEXT
            )
        ''')
        self.conn.commit()
    
    def save_scan(self, target, scan_type, open_ports, ml_risk, results):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO scans (target, date, scan_type, open_ports, ml_risk, results)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (target, datetime.now().isoformat(), scan_type, open_ports, ml_risk, json.dumps(results[:1000])))
        self.conn.commit()
        print(f"[💾] Escaneo guardado en base de datos (ID: {cursor.lastrowid})")
    
    def get_history(self, limit=10):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, target, date, scan_type, open_ports, ml_risk FROM scans ORDER BY id DESC LIMIT ?', (limit,))
        return cursor.fetchall()
    
    def close(self):
        self.conn.close()
