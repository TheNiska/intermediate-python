1. Primary keys can be circular. A key can point to another table that has a key that poinst at the first table. A key can even point at a row of the same table.
2. A primary key can be composite: compound of several columns. Used if any one column  cannot uniquely identify a row.
3. Two foregn key as a primay key used often to create many-to-many relationship.

# Subsets of SQL
1. Data Definition Language (__DDL__) -- The SQL DDL category provides commands for defining, deleting and modifying tables in a database.  
2. Data Query Language (__DQL__)  -- The SQL DQL commands provide the ability to query and retrieve data from the database.  
3. Data Manipulation Language (__DML__)  -- The SQL DML commands provide the ability to query, delete and update data in the database.  
4. Data Control Language (__DCL__) -- You use DCL to deal with the rights and permissions of users of a database system.  
5. Transaction Control Language (__TCL__) -- The TCL commands are used to manage transactions in the database. These are used to manage the changes made to the data in a table by utilizing the DML commands.  

# Data normalization
### First normal form
The first normal form enforces data atomicity and eliminates unnecessary repeating data groups. A table can only have one single instance value of the column attribute in any table cell.  

### Second normal form
In the second normal form, you must avoid partial dependency relationships between data. Partial dependency refers to tables with a composite primary key. Namely, a key that consists of a combination of two or more columns, where a non-key attribute value depends only on one part of the composite key.  

### Third normal form
The third normal form states that a table must have no transitive dependency. This means that any non-key attribute in a table may not be functionally dependent on another non-key attribute in the same table.  


