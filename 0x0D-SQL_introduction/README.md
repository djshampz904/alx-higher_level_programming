# SQL introdution 

## Introduction

SQL (Structured Query Language) is a standard language for storing, manipulating and retrieving data in databases. SQL was first developed at IBM in the early 1970s. It is a standard language for relational database management systems. SQL is used to perform all types of data operations in a database. It is widely used in data science and data analysis.

## 0-list_databases.sql

script that lists all databases of your MySQL server.

bash
```
$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

## 1-create_database_if_missing.sql

script that creates the database hbtn_0c_0 in your MySQL server.

bash
```
$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
```

## 2-remove_database.sql

script that deletes the database hbtn_0c_0 in your MySQL server.

bash
```
$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
```

