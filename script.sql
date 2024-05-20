DROP DATABASE IF EXISTS bd_api_pymes_insurance;
CREATE DATABASE bd_api_pymes_insurance CHARSET utf8mb4;
USE bd_api_pymes_insurance;

CREATE TABLE PYME(
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    coverage VARCHAR(100) NOT NULL,
    premium DECIMAL(10, 2) NOT NULL,
    deductible DECIMAL(10, 2) NOT NULL,
    coverage_limit DECIMAL(10, 2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    company VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100) NOT NULL,
    contact_phone VARCHAR(20) NOT NULL,
    quotationId INT(11) NOT NULL, 
    PRIMARY KEY (id)
);