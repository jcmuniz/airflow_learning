# Airflow Learning
> This repository is used to study Apache Airflow deploy with Kubernetes on Minikube (vm=Docker)

<code><img height="20" src="https://img.shields.io/badge/Git-F05032?style=plastic&logo=git&logoColor=white"/></code>
<code><img height="20" src="https://img.shields.io/badge/Python-3776AB?style=plastic&logo=python&logoColor=white"/></code>
<code><img height="20" src="https://img.shields.io/badge/Airflow-017CEE?style=plastic&logo=Apache%20Airflow&logoColor=white"/></code>
<code><img height="20" src="https://img.shields.io/badge/PostgreSQL-316192?style=plastic&logo=postgresql&logoColor=white"/></code>
<code><img height="20" src="https://img.shields.io/badge/redis-%23DD0031.svg?&style=plastic&logo=redis&logoColor=white"/></code>
<code><img height="20" src="https://img.shields.io/badge/kubernetes-326ce5.svg?style=plastic&logo=kubernetes&logoColor=white"/></code>
<code><img height="20" src="https://img.shields.io/badge/Docker-2CA5E0?style=plastic&logo=docker&logoColor=white"/></code>

## Requirements

* docker
* minikube
* kubernetes-cli / kubectl

## Deployment setup

Start minikube and dashboard (_optimal_):

```sh
minikube start --kubernetes-version=v1.21.4
minikube dashboard
```

Apply these deployments following the order:

```sh
kubectl apply -f airflow_db_deployment.yaml
kubectl apply -f airflow_base_deployment.yaml
kubectl apply -f airflow_workers_deployment.yaml
```

## Usage

To enter Apache Airflow UI, just run the follow command and start to develop your DAGs:

```sh
minikube service airflow
```

Or you can run a port-forward after get the podName and access using http://localhost:8080 :

```sh
kubectl port-forward _podName_ 8080:8080
```

## Monitoring the workers

If you would like to monitor the workers, you can run this:

```sh
minikube service flower
```

You can do the same step used in port-forward above and access using http://localhost:5555 :

```sh
- kubectl port-forward airflow-base-<hash> 5555:5555
```

## About Me

Juliano Muniz 
[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/jcmuniz)]




