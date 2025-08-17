# simple sql, fast api server
- A service that returns to GET request all the information that exists in the table.


# Project Features
- The MySQL database is run using OpenShift.
- Access layer to data.
- Server in FastAPI - Accesses MySQL and returns the table data to a dedicated endpoint.

# project structure

- data-loader/
- ├── services/
- │ └── data_loader.py # Data loading service
- | └── app.py #End point service
- ├── scripts/ # SQL scripts, OS scripts
- ├── infrastructure/
- │ └── k8s/ # Kubernetes manifests (YAMLs)
- ├── Dockerfile
- ├── requirements.txt
- └── README.md