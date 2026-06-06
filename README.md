# MBL Dental Clinic Inventory System

## Overview

This project is a Dental Clinic Inventory Management System developed using Python, Flask, MySQL, HTML, and CSS. The system allows dental clinic staff to manage and monitor dental supplies and materials efficiently. Users can view inventory items, add new supplies, update existing records, delete items, and track inventory transactions.

The system stores data in a MySQL relational database and uses SQL queries to interact with the database. To demonstrate relational database concepts, the project includes two related tables: **supplies** and **transactions**. A SQL JOIN query is used to display transaction history together with the corresponding supply information.

I created this project to practice working with relational databases, SQL commands, Flask web development, database connectivity, CRUD operations (Create, Read, Update, Delete), and SQL JOIN queries while building a real-world application that could be used in a dental clinic environment.

## Software Demo Video

[Software Demo Video](https://www.youtube.com/watch?v=XylahOoT24U)

## Development Environment

* Python 3
* Flask
* MySQL
* MySQL Workbench
* HTML
* CSS
* Visual Studio Code
* GitHub

## Features

* View all dental inventory items
* Add new supply items
* Edit existing supply records
* Delete inventory items
* Display total inventory count
* Store inventory information in MySQL
* Track inventory transactions
* Display transaction history
* SQL JOIN between supplies and transactions tables

## Database Structure

### Supplies Table

Stores information about dental supplies including:

* Item Name
* Category
* Quantity
* Unit
* Minimum Stock Level
* Date Updated

### Transactions Table

Stores inventory transaction records including:

* Supply ID
* Transaction Type
* Quantity
* Transaction Date

The two tables are connected through a foreign key relationship using the Supply ID field.

## Stretch Challenge

I completed the stretch challenge by creating an additional table called **transactions** and performing a SQL JOIN query between the **supplies** and **transactions** tables. This allows the application to display transaction history along with the corresponding supply names and inventory information.

## AI Disclosure

I used ChatGPT to help me learn Flask, MySQL database connectivity, SQL queries, HTML/CSS styling, and debugging techniques throughout the development process.

I used AI-generated examples and explanations to better understand CRUD operations, SQL JOIN statements, Flask routing, database integration, and user interface design. I customized the database structure, inventory categories, dental supply data, application layout, styling, and overall project organization to fit the needs of a dental clinic inventory management system.

Using AI helped me understand relational database concepts and web development practices while allowing me to build and personalize the project based on my own learning goals.
