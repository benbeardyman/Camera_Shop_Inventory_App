from db.run_sql import run_sql

from models.manufacturer import Manufacturer

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name) VALUES ( %s ) RETURNING id"
    values = [manufacturer.name]
    results = run_sql(sql, values)
    manufacturer.id = results[0]['id']
    return manufacturer

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)
    for row in results:
        manufacturer = Manufacturer(row['name'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers

# 1. Create manufacturer variable and define as None
# 2. Create SQL variable and assign as SQL string with select all query selecting from manufacturers table where id in table is same as input id
# 3. Create vaules variable and assign as a list containing input id
# 4. Create result variable running the SQL query giving the first result to the variable
# 5. If query gives a result (result is not None) create instance of Manufacturer
# 6. Return manufacturer variable

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['name'], result['id'])
    return manufacturer

def update(manufacturer):
    sql = "UPDATE manufacturers SET name = %s WHERE id = %s"
    values = [manufacturer.name, manufacturer.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

    