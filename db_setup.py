
import sqlite3

try:
    print("Database Connection")
    db = sqlite3.connect("inventory.db") # Creo base de datos. ":memory:" si quiero que se borre, solo sea en memoria. Pero no es el caso.

    # print("Create Cursor"
    # cursor = conn.cursor()

    print("Create Table")
    db.execute("DROP TABLE IF EXISTS part_inventory_app")   #Si existe la tabla, borrela. Esto para inicar desde cero.
    db.execute(
        "CREATE TABLE part_inventory_app (part_no VARCHAR PRIMARY KEY, quant INTEGER)"      #Creo tabla con 2 columnas. La KEY que no debe repetirse, INTEGER que es numero.
    )

    print("Insert Data")
    data = [                                #Creo lista de tublas con elementos a insertar en la base.
        ("a42CLDR", 18194),
        ("b42CLDR", 18362),
        ("c42CLDR", 12362),
        ("d42CLDR", 128),
        ("e42CLDR", 1228),
    ]
    db.executemany("INSERT INTO part_inventory_app VALUES (?,?)", data) #executemany para que haga el ciclo for sobre cada tupla.
    #Reemplaza en cada ?? los valores del data.
    db.commit()     #para grabarlo

    print("Close Connection")
    db.close() #Debo cerrarlo

except Exception as e: #Si hay error, muestre cual y pongalo en pantalla
    print(f"\tERROR: {str(e)}", flush=True)
    

    