# kubernetes-airflow
Repository to deploy Apache Airflow on kubernetes

## Installation

Prior to deploy the Airflow chart, a running database must be deployed. Use the following repository to deploy a Postgres database:
https://github.com/hfolguera/kubernetes-airflow-postgres


1. Add the Aiflow helm repo
```
helm repo add apache-airflow https://airflow.apache.org
helm repo update
helm search repo airflow
```

3. Generate the values file
```
helm show values apache-airflow/airflow > values.yaml
```

Customizations:
- Use Kubernetes executor
- Use LoadBalancer type for webserver service
- Configure database connection data

4. Deploy airflow
```
helm upgrade --install airflow apache-airflow/airflow -n airflow --create-namespace -f values.yaml --debug
```

5. Verify deployment
```
helm ls -n airflow
kubectl get all -n airflow
```
