Find the author with the name 'Kara Melton' and then select all the articles she has written.

SELECT * FROM authors;
SELECT title FROM articles WHERE id = 8;
                   title                   
-------------------------------------------
 Making Tech Spaces Safe for Diverse Faces

Find Ontario in the provinces table and then find all the cities in that province.

SELECT name FROM cities WHERE province_id = 14;
name   
---------
 Toronto
 Ottawa

Who wrote the article called 'Coding Bootcamps and Emotional Labor'?

SELECT author_id FROM articles WHERE title = 'Coding Bootcamps and Emotional Labor';
SELECT name FROM authors WHERE id = 4;

       name        
-------------------
 Tilde Ann Thurium

Write a series of SQL queries to find out how many provinces are in Canada.

SELECT * FROM provinces;
13

How many people live at 4740 McDermott Street?

SELECT * FROM residences;
SELECT name FROM persons WHERE residence_id = 9;

What city is 4740 McDermott Street in?

SELECT * FROM residences;
SELECT name FROM cities WHERE id = 11;
  name  
--------
 Ottawa

What province is 4740 McDermott Street in?

SELECT name FROM provinces WHERE id = 14;

What country is 4740 McDermott Street in?

SELECT * FROM countries;

 id |  name  | year_founded | national_animal 
----+--------+--------------+-----------------
  1 | Canada |         1867 | beaver


Find the person named 'Destini Davis' and then use a series of SQL queries to find what country they live in.

SELECT * FROM persons WHERE name = 'Destini Davis';
SELECT * FROM countries;

 id |  name  | year_founded | national_animal 
----+--------+--------------+-----------------
  1 | Canada |         1867 | beaver


How many articles has Aditya Mukerjee written?

SELECT * FROM authors WHERE name = 'Aditya Mukerjee';
SELECT title FROM articles WHERE author_id = 2;

                          title                          
---------------------------------------------------------
 I Can Text You A Pile of Poo, But I Can’t Write My Name