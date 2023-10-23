- CREATE TABLE table_name (column_name1 datatype(size), column_name2 datatype(size), column_name3 datatype(size));
- DROP TABLE table_name;
- ALTER TABLE table_name ADD (column_name datatype(size));
- ALTER TABLE table_name ADD primary key (column_name);
- TRUNCATE TABLE table_name;
- SELECT * FROM table_name;
- INSERT INTO table_name (column1, column2, column3) VALUES (value1, value2, value3);
- UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
- DELETE FROM table_name WHERE condition;
- GRANT Command to provide the user of the database with the privileges required to allow users to access and manipulate the database.
- REVOKE Command to remove permissions from any user.
- COMMIT Command to save all the work you have already done in the database.
- ROLLBACK Command to restore a database to the last committed state.
- INSERT INTO table_name (column_name) SELECT column_name2 FROM table_name2; -- inserting column from one table to another.  

## Arithmetic operators examples
- SELECT column_name1 + column_name2 FROM table_name;  
- SELECT * FROM employee WHERE salary - tax = 50000;  

## Filternig data
- SELECT column1, column2, columnN FROM table_name WHERE [condition1] AND [condition2]...AND [conditionN];  
- SELECT DISTINCT BillingCountry FROM invoices ORDER BY BillingCountry;  
