# schemas.py

from pydantic import BaseModel
from datetime import date 
from decimal import Decimal

# Definir el esquema de datos para las pólizas de seguro
class PymeInput(BaseModel):
    quotationId: int
    name: str
    description: str
    coverage: str
    premium: float
    deductible: float
    coverage_limit: float
    start_date: date
    end_date: date
    company: str
    contact_person: str
    contact_email: str
    contact_phone: int
    
class PymeOutput(BaseModel):
    id: int
    quotationId: int
    name: str
    detail: str
    coverage: str
    premium: Decimal
    deductible: Decimal
    sum_assured: Decimal
    start_date: date
    end_date: date
    company: str
    contact_name: str
    contact_email: str
    contact_phone: str
    
