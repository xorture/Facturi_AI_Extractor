import sqlite3

def creeaza_baza_de_date():

    conn = sqlite3.connect('facturi.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS facturi_procesate (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            furnizor TEXT,
            cui_furnizor TEXT,
            data_factura TEXT,
            suma_totala REAL,
            tva REAL,
            stare_procesare TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print("Baza de date 'facturi.db' a fost creata cu succes! Suntem gata sa bagam date in ea.")

if __name__ == '__main__':
    creeaza_baza_de_date()