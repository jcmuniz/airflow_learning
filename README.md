# Apache Airflow - Learning
> This repository is used to study about Apache Airflow deployed with Kubernetes on Minikube (driver=Docker)

<code><img height="20" src="https://img.shields.io/badge/Git-F05032?style=plastic&logo=git&logoColor=white"/></code>
<code><img height="20" src="https://img.shields.io/badge/Python-3776AB?style=plastic&logo=python&logoColor=white"/></code>
<code><img height="20" src="https://img.shields.io/badge/Airflow-017CEE?style=plastic&logo=Apache%20Airflow&logoColor=white"/></code>
<code><img height="20" src="https://img.shields.io/badge/PostgreSQL-316192?style=plastic&logo=postgresql&logoColor=white"/></code>
<code><img height="20" src="https://img.shields.io/badge/redis-%23DD0031.svg?&style=plastic&logo=redis&logoColor=white"/></code>
<code><img height="20" src="https://img.shields.io/badge/kubernetes-326ce5.svg?style=plastic&logo=kubernetes&logoColor=white"/></code>
<code><img height="20" src="https://img.shields.io/badge/Docker-2CA5E0?style=plastic&logo=docker&logoColor=white"/></code>

## Requirements

* docker (https://docs.docker.com/get-docker/)
* minikube (https://minikube.sigs.k8s.io/docs/start/)
* kubernetes-cli / kubectl (https://kubernetes.io/docs/tasks/tools/)

## Deployment setup

Start minikube:

```sh
minikube start --kubernetes-version=v1.21.4
```

And dashboard (_optimal_):
```sh
minikube dashboard
```

Apply these deployments following the order:

```sh
kubectl apply -f ./infra/k8s/airflow_db_deployment.yaml
kubectl apply -f ./infra/k8s/airflow_base_deployment.yaml
kubectl apply -f ./infra/k8s/airflow_workers_deployment.yaml
```

## Usage

To enter Apache Airflow UI, just run the follow command and start to develop your DAGs:

```sh
minikube service airflow
```

Or you can do a port-forward after get the podName of airflow-base and access using http://localhost:8080 :

```sh
kubectl get pods
kubectl port-forward <podName> 8080:8080
```

## Monitoring the workers

If you would like to monitor the workers, you can run this:

```sh
minikube service flower
```

You can do the same step used in port-forward above and accessing http://localhost:5555 :

```sh
kubectl get pods
kubectl port-forward <podName> 5555:5555
```

## About Me

Juliano Muniz 
[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/jcmuniz)](https://github.com/jcmuniz)




