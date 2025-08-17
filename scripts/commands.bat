oc new-app mysql-ephemeral --name=mysql-db -p MYSQL_USER=user -p MYSQL_PASSWORD=pwd -p MYSQL_DATABASE=mydb

oc rsh mysql-1-hml6b

mysql -u user -p mydb


CREATE TABLE Names (id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(50),city VARCHAR(50));

INSERT INTO Names (name, city) VALUES ('Dan', 'Tel-aviv'),('Beni', 'Bni-brak'),('Or', 'Hifa');

oc new-app https://github.com/Shlomo-kodkod/OpenShift-sql-docker --name dataserver-v1

