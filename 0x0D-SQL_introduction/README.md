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

## 3-list_tables.sql

script that lists all the tables of a database in your MySQL server.

bash
```
$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## 4-first_table.sql

script that creates a table called first_table in the current database in your MySQL server.

bash
```
$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## 5-full_table.sql

script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

bash
```
$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## 6-list_values.sql

script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

bash
```
$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## 7-insert_value.sql

script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

bash
```
$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## 8-count_89.sql

script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

bash
```
$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## 9-full_creation.sql

script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

bash
```
$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## 10-top_score.sql

script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

bash
```
$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## 11-best_score.sql

script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

bash
```
$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## 12-no_cheating.sql

script that updates the score of Bob to 10 in the table second_table.

bash
```
$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## 13-change_class.sql

script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

bash
```

$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## 14-average.sql

script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

bash
```
$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## 15-groups.sql

script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

bash
```
$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## 16-no_link.sql

script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

bash
```
$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```
