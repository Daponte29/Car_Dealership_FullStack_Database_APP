-- Create DB, user and grant permissions
CREATE USER IF NOT EXISTS gtuser@'%' IDENTIFIED BY 'team099';
DROP DATABASE IF EXISTS `cs6400-fa23-team099_Demo`;
SET default_storage_engine=InnoDB;
SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE DATABASE IF NOT EXISTS `cs6400-fa23-team099_Demo`
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_unicode_ci;

USE `cs6400-fa23-team099_Demo`;
GRANT ALL ON `cs6400-fa23-team099_Demo`.* TO 'gtuser'@'%';
FLUSH PRIVILEGES;


------------
-- Tables --
------------

-- User
CREATE TABLE User(
    userID INTEGER NOT NULL AUTO_INCREMENT,
	username VARCHAR(15) NOT NULL,
	password VARCHAR(30) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50) NOT NULL,
    UNIQUE(username),
    PRIMARY KEY(userID)
);

-- InventoryCLerk
CREATE TABLE InventoryClerk(
    userID INTEGER NOT NULL,
    UNIQUE(userID)
);

-- SalesPerson
CREATE TABLE SalesPerson(
    userID INTEGER NOT NULL,
    UNIQUE(userID)
);

-- Manager
CREATE TABLE Manager(
    userID INTEGER NOT NULL,
    UNIQUE(userID)
);

-- Customer
CREATE TABLE Customer(
    customerID INTEGER NOT NULL AUTO_INCREMENT,
    email VARCHAR(50),
    postal_code VARCHAR(5) NOT NULL,
    state VARCHAR(30) NOT NULL,
    city VARCHAR(30) NOT NULL,
    street VARCHAR(80) NOT NULL,
    phone_number VARCHAR(30) NOT NULL,
    PRIMARY KEY(customerID)
);

-- Individual
CREATE TABLE Individual(
    license_number VARCHAR(20) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    customerID INTEGER NOT NULL,
    PRIMARY KEY(license_number)
);

-- Business
CREATE TABLE Business(
    tin VARCHAR(9),
    business_name VARCHAR(100) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    title VARCHAR(30) NOT NULL,
    customerID INTEGER NOT NULL,
    PRIMARY KEY(tin)
);

-- InventoryClerk_Customer relationship M:N
CREATE TABLE InventoryClerk_Customer(
    userID INTEGER NOT NULL,
    customerID INTEGER NOT NULL
);

-- Purchase
CREATE TABLE Purchase(
    purchaseID INTEGER NOT NULL AUTO_INCREMENT,
    purchase_date DATE NOT NULL,
    condition_at_purchase VARCHAR(10) NOT NULL,
    purchase_price FLOAT(10, 2) NOT NULL,
    userID INTEGER NOT NULL,
    vin VARCHAR(20) NOT NULL,
    customerID INTEGER NOT NULL,
    PRIMARY KEY(purchaseID)
);

-- Sale
CREATE TABLE Sale(
    saleID INTEGER NOT NULL AUTO_INCREMENT,
    sale_price FLOAT(10,2) NOT NULL,
    sale_date DATE NOT NULL,
    userID INTEGER NOT NULL,
    vin VARCHAR(20) NOT NULL,
    customerID INTEGER NOT NULL,
    PRIMARY KEY(saleID)
);

-- VehicleManufacturer
CREATE TABLE VehicleManufacturer(
    manufacturer VARCHAR(50) NOT NULL,
    PRIMARY KEY(manufacturer)
);

CREATE TABLE Color(
    color_name VARCHAR(50) NOT NULL,
    PRIMARY KEY(color_name)
);
CREATE TABLE VehicleType(
    type VARCHAR(50) NOT NULL,
    PRIMARY KEY(type)
);

-- Vehicle
CREATE TABLE Vehicle(
    vin VARCHAR(20) NOT NULL,
    model_name VARCHAR(50) NOT NULL,
    model_year INTEGER NOT NULL,
    fuel_type VARCHAR(15) NOT NULL,
    mileage INTEGER NOT NULL,
    description VARCHAR(255),
    manufacturer VARCHAR(50) NOT NULL,
    type VARCHAR(50) NOT NULL,
    PRIMARY KEY(vin)
);


CREATE TABLE Vehicle_Color(
    color_name VARCHAR(50) NOT NULL,
    vin VARCHAR(20) NOT NULL
	PRIMARY KEY(vin, color_name)
);


-- Vendor

CREATE TABLE Vendor(
    vendor_name VARCHAR(20) NOT NULL,
    phone_number VARCHAR(30) NOT NULL,
    street VARCHAR(50) NOT NULL,
    city VARCHAR(30) NOT NULL,
    state VARCHAR(20) NOT NULL,
    postal_code VARCHAR(5) NOT NULL,
    PRIMARY KEY(vendor_name)
);

-- Part
CREATE TABLE Part(
    part_number VARCHAR(30) NOT NULL,
    part_status VARCHAR(10) NOT NULL,
    description VARCHAR(255) NOT NULL,
    cost_of_part FLOAT(10,2) NOT NULL,
    quantity INTEGER NOT NULL,
    purchase_order_number VARCHAR(30) NOT NULL,
	vin VARCHAR(20) NOT NULL,
    PRIMARY KEY(part_number,purchase_order_number,vin)
);

-- PartsOrder
CREATE TABLE PartsOrder(
    purchase_order_number VARCHAR(30) NOT NULL,
    vin VARCHAR(20) NOT NULL,
    vendor_name VARCHAR(20) NOT NULL,
    PRIMARY KEY(purchase_order_number)
);
--------------------
-- FK Constraints --
--------------------

ALTER TABLE InventoryClerk ADD CONSTRAINT fk_InventoryClerk_userID_User_userID FOREIGN KEY (userID) REFERENCES User(userID);
ALTER TABLE SalesPerson ADD CONSTRAINT fk_SalesPerson_userID_User_userID FOREIGN KEY (userID) REFERENCES User(userID);
ALTER TABLE Manager ADD CONSTRAINT fk_Manager_userID_User_userID FOREIGN KEY (userID) REFERENCES User(userID);

ALTER TABLE Individual ADD CONSTRAINT fk_Individual_customerID_Customer_customerID FOREIGN KEY (customerID) REFERENCES Customer(customerID);
ALTER TABLE Business ADD CONSTRAINT fk_Business_customerID_Customer_customerID FOREIGN KEY (customerID) REFERENCES Customer(customerID);

ALTER TABLE InventoryClerk_Customer ADD CONSTRAINT fk_InventoryClerk_Customer_userID_User_userID FOREIGN KEY (userID) REFERENCES InventoryClerk(userID);
ALTER TABLE InventoryClerk_Customer ADD CONSTRAINT fk_InventoryClerk_Customer_customerID_Customer_customerID FOREIGN KEY (customerID) REFERENCES Customer(customerID);

ALTER TABLE Purchase ADD CONSTRAINT fk_Purchase_customerID_Customer_customerID FOREIGN KEY (customerID) REFERENCES Customer(customerID);
ALTER TABLE Purchase ADD CONSTRAINT fk_Purchase_vin_Vehicle_vin FOREIGN KEY (vin) REFERENCES Vehicle(vin);
ALTER TABLE Purchase ADD CONSTRAINT fk_Purchase_userID_InventoryClerk_userID FOREIGN KEY (userID) REFERENCES InventoryClerk(userID);

ALTER TABLE Sale ADD CONSTRAINT fk_Sale_customerID_Customer_customerID FOREIGN KEY (customerID) REFERENCES Customer(customerID);
ALTER TABLE Sale ADD CONSTRAINT fk_Sale_vin_Vehicle_vin FOREIGN KEY (vin) REFERENCES Vehicle(vin);
ALTER TABLE Sale ADD CONSTRAINT fk_Sale_userID_salesPerson_userID FOREIGN KEY (userID) REFERENCES SalesPerson(userID);

ALTER TABLE Vehicle ADD CONSTRAINT fk_Vehicle_manufacturer_VehicleManufacturer_manufacturer FOREIGN KEY (manufacturer) REFERENCES VehicleManufacturer(manufacturer);
ALTER TABLE Vehicle ADD CONSTRAINT fk_Vehicle_type_VehicleType_type FOREIGN KEY (type) REFERENCES VehicleType(type);

ALTER TABLE Vehicle_Color ADD CONSTRAINT fk_Vehicle_Color_color_name_Color_color_name FOREIGN KEY (color_name) REFERENCES Color(color_name);
ALTER TABLE Vehicle_Color ADD CONSTRAINT fk_Vehicle_Color_vin_Vehicle_vin FOREIGN KEY (vin) REFERENCES Vehicle(vin);

ALTER TABLE PartsOrder ADD CONSTRAINT fk_PartsOrder_vin_Vehicle_vin FOREIGN KEY (vin) REFERENCES Vehicle(vin);
ALTER TABLE PartsOrder ADD CONSTRAINT fk_PartsOrder_name_Vendor_name FOREIGN KEY (vendor_name) REFERENCES Vendor(vendor_name);

ALTER TABLE Part ADD CONSTRAINT fk_Part_purchase_order_number_PartsOrder_purchase_order_number FOREIGN KEY (purchase_order_number) REFERENCES PartsOrder(purchase_order_number);