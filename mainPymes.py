# main.py

from fastapi import FastAPI, HTTPException, status, Response
import mysql.connector
import schemas
from typing import List
import uuid

app = FastAPI()

# Configuración de la base de datos
host_name = "34.236.117.148"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_api_pymes_insurance"

# Conectar a la base de datos
mydb = mysql.connector.connect(
    host=host_name,
    port=port_number,
    user=user_name,
    password=password_db,
    database=database_name
)

# Endpoint para obtener todas las datos
@app.get("/api/v1/pymes/", response_model=List[schemas.PymeOutput])
def get_pyme_insurance_policies(response: Response):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM PYME")
    pymes = cursor.fetchall()
    cursor.close()
    
    if not pymes:
        response.status_code = status.HTTP_204_NO_CONTENT
        return []

    # Mapeo de los datos de la base de datos al esquema PymeOutput
    result = []
    for pyme in pymes:
        pyme_dict = {
            'id': pyme[0],
            'name': pyme[1],
            'detail': pyme[2],
            'coverage': pyme[3],
            'premium': pyme[4],
            'deductible': pyme[5],
            'sum_assured': pyme[6],
            'start_date': pyme[7],
            'end_date': pyme[8],
            'company': pyme[9],
            'contact_name': pyme[10],
            'contact_email': pyme[11],
            'contact_phone': pyme[12],
            'quotationId': pyme[13]
            
        }
        result.append(schemas.PymeOutput(**pyme_dict))
    
    return result

# Endpoint para obtener una pyme de seguro por ID
@app.get("/api/v1/pyme/{id}", response_model=schemas.PymeOutput)
def get_pyme_insurance_policy(id: int):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM PYME WHERE id = %s", (id,))
    pyme = cursor.fetchone()
    cursor.close()
    if not pyme:
        raise HTTPException(status_code=404, detail="Pyme not found")

    # Mapeo de la tupla a un diccionario con las claves adecuadas
    pyme_dict = {
        'id': pyme[0],
        'name': pyme[1],
        'detail': pyme[2],
        'coverage': pyme[3],
        'premium': pyme[4],
        'deductible': pyme[5],
        'sum_assured': pyme[6],
        'start_date': pyme[7],
        'end_date': pyme[8],
        'company': pyme[9],
        'contact_name': pyme[10],
        'contact_email': pyme[11],
        'contact_phone': pyme[12],
        'quotationId': pyme[13]
    }
    return schemas.PymeOutput(**pyme_dict)

# Endpoint para crear una nueva póliza de seguro
@app.post("/api/v1/pyme/")
def create_pyme_insurance_policy(item: schemas.PymeInput):
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO PYME (name, description, coverage, premium, deductible, coverage_limit, start_date, end_date, company, contact_person, contact_email, contact_phone, quotationId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (item.name, item.description, item.coverage, item.premium, item.deductible, item.coverage_limit, item.start_date, item.end_date, item.company, item.contact_person, item.contact_email, item.contact_phone, item.quotationId))
    mydb.commit()
    cursor.close()
    return {"message": "Pyme created successfully"}


# Endpoint para actualizar una póliza de seguro existente
@app.put("/api/v1/pyme/{id}")
def update_pyme_insurance_policy(id: int, policy: schemas.PymeInput):
    cursor = mydb.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM PYME WHERE id = %s", (id,))
    if cursor.fetchone()[0] == 0:
        trace_id = str(uuid.uuid4())
        raise HTTPException(
            status_code=404,
            detail={
                "error-code": "ERR0030",
                "error-message": "Error, id not found",
                "trace-id": trace_id,
            }
        )
    
    cursor.execute("UPDATE PYME SET name = %s, description = %s, coverage = %s, premium = %s, deductible = %s, coverage_limit = %s, start_date = %s, end_date = %s, company = %s, contact_person = %s, contact_email = %s, contact_phone = %s, quotationId = %s WHERE id = %s",
                   (policy.name, policy.description, policy.coverage, policy.premium, policy.deductible, policy.coverage_limit, policy.start_date, policy.end_date, policy.company, policy.contact_person, policy.contact_email, policy.contact_phone, policy.quotationId, id))
    mydb.commit()
    cursor.close()
    return {"message": "PYME updated successfully"}

# Endpoint para eliminar una póliza de seguro por ID
@app.delete("/api/v1/pyme/{id}")
def delete_pyme_insurance_policy(id: int):
    cursor = mydb.cursor()
    cursor.execute("SELECT COUNT(*) FROM PYME WHERE id = %s", (id,))
    if cursor.fetchone()[0] == 0:
        trace_id = str(uuid.uuid4())
        raise HTTPException(
            status_code=404,
            detail={
                "error-code": "ERR0030",
                "error-message": "Error, id not found",
                "trace-id": trace_id,
            }
        )
        
    cursor.execute("DELETE FROM PYME WHERE id = %s", (id,))
    mydb.commit()
    cursor.close()
    return {"message": "PYME deleted successfully"}
