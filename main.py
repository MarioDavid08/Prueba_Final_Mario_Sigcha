from selenium import webdriver
from selenium.webdriver.common.by import By
from mongo import MongoConnection


db_client = MongoConnection().client
db = db_client.get_database('clasificacion')
col = db.get_collection('pilots_panel_f1')


driver = webdriver.Chrome()
driver.get("https://resultados.as.com/resultados/motor/formula_1/clasificacion/")
pilots_panel_f1 = driver.find_elements(By.CLASS_NAME, "row-table-datos")
print("Clasificación general de pilotos y escuderías de Fórmula 1")
for f in pilots_panel_f1:
    pos_pilots_name = f.find_element(by=By.CLASS_NAME, value="main-name-in-table").accessible_name
    print(pos_pilots_name)
    punt_name = f.find_element(by=By.CLASS_NAME, value="destacado").accessible_name
    print(" ",punt_name, "puntos")
    print('-' * 20)

    document = {
        "posición pilotos": pos_pilots_name,
        "puntos": punt_name,
    }
    col.insert_one(document=document)


col = db.get_collection('pilots_panel_moto_GP')
driver = webdriver.Chrome()
driver.get("https://resultados.as.com/resultados/motor/motogp/clasificacion/")
pilots_panel_gp = driver.find_elements(By.CLASS_NAME, "row-table-datos")
print("Clasificación general de pilotos y escuderías de Moto GP")
for f in pilots_panel_gp:
    pos_pilots_name = f.find_element(by=By.CLASS_NAME, value="main-name-in-table").accessible_name
    print(pos_pilots_name)
    punt_name = f.find_element(by=By.CLASS_NAME, value="destacado").accessible_name
    print(" ",punt_name, "puntos")
    print('-' * 20)

    document = {
        "posición pilotos": pos_pilots_name,
        "puntos": punt_name,
    }

    col.insert_one(document=document)


driver.close()