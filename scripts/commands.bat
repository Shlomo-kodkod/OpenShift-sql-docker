
oc new-app --name=mysql-db  -e MYSQL_USER=user -e MYSQL_PASSWORD=pwd -e MYSQL_DATABASE=mydb mysql:8.0

 
oc new-app mysql-persistent -e MYSQL_USER=user -e MYSQL_PASSWORD=pwd -e MYSQL_DATABASE=mydb 

oc set volumes deployment mysql-db --add --mount-path=/mypvc --name=mypvc --claim-name=mypvc --read-only=false --type=persistentVolumeClaim --claim-size=1Gi

oc get pods 

oc rsh mysql-db-79ccd69f57-ds7l4

mysql -u user -p mydb

CREATE TABLE Names (id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(50),city VARCHAR(50));

INSERT INTO Names (name, city) VALUES ('Dan', 'Tel-aviv'),('Beni', 'Bni-brak'),('Or', 'Hifa');

exit

exit 

oc new-app https://github.com/Shlomo-kodkod/OpenShift-sql-docker#main

oc get deployment

oc expose deployment openshift-sql-docker --name=fastapi --port=8080

oc get service

oc expose service fastapi

oc get routes


