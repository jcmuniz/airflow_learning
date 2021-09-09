# Airflow Learning
This repository is used to study Apache Airflow deploy with Kubernetes on Minikube

Start minikube:
- minikube start --kubernetes-version=v1.21.4

Change the FERNET_KEY, apply the deployments in below order and enjoy!
1) db
2) base
3) worker

---------------------------------------------------------------------------------------------

To access the airflow ui and flower you have these ways:
1) Port-forward:
kubectl port-forward <podName> <localPort>:<remotePort>
- kubectl port-forward airflow-base-<hash> 8080:8080
- kubectl port-forward airflow-base-<hash> 5555:5555

2) Minikube (easy way): 
minikube service <serviceName>
- minikube service airflow
- minikube service flower

