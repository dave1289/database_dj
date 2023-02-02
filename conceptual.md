### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
object relational database.  Allows us to use server side objects to access DB values.

- What is the difference between SQL and PostgreSQL?
SQL is the base language while postgres is a framework that gives us enhanced capabilities.

- In `psql`, how do you connect to a database?
\c <database name>

- What is the difference between `HAVING` and `WHERE`?
Where cannot be used with aggregate functions while having can.

- What is the difference between an `INNER` and `OUTER` join?
Inner join will only join overlap outer join will join all elements from one "side" of the join.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
Determines which table (first or second) will be fleshed out beyond overlap

- What is an ORM? What do they do?
object relation mapping.  this gives us an object oriented method to access our DB info.  I.E. flask-sqlalchemy.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  AJAX has functionality without refresh, all server side needs a refresh for the page.

- What is CSRF? What is the purpose of the CSRF token?
CSRF is a token that is sent with form verification to ensure access is restricted/allowed as needed.

- What is the purpose of `form.hidden_tag()`?
This hides our hidden aspects of the form, i.e. CSRF token
