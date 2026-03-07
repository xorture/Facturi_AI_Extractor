import sqlite3

# ne conectam la fisierul creat adineauri
conn = sqlite3.connect('facturi.db')
cursor = conn.cursor()

# 1. INSERAM o factura fake in sistem (ca si cum ar fi extras-o AI-ul)
cursor.execute('''
    INSERT INTO facturi_procesate (furnizor, cui_furnizor, data_factura, suma_totala, tva, stare_procesare)
    VALUES ('eMAG S.R.L.', 'RO14399840', '2026-02-24', 3500.50, 665.09, 'Succes')
''')

# salvam modificarea
conn.commit()

# 2. CITIM din baza de date sa vedem daca s-a salvat
cursor.execute('SELECT furnizor, suma_totala, stare_procesare FROM facturi_procesate')
toate_facturile = cursor.fetchall()

print("--- REZULTAT DIN BAZA DE DATE ---")
for factura in toate_facturile:
    print(f"Am gasit factura de la {factura[0]} in valoare de {factura[1]} RON. Status: {factura[2]}")

conn.close()