# yaml-extractor
## Prerequisites
- Python3 
- Docker for desktop [docker](https://docs.docker.com/desktop/mac/install/)
- Docker compose [docker-compose](https://docs.docker.com/compose/install/)
- Install [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- Install [helm](https://www.consul.io/docs/k8s/helm)

## Run tool as cli
Add /cli/cli.py to you $PATH
```bash
echo $PATH
mv ./cli/cli.py <Folder on you $PATH>
```
## Build image
1. docker build -t web-api:0.1.0 . 

## Run app with docker-compose
docker-compose up -d

## Kubernetes (Run local machine)
1. Make sure you have local k8s cluster running with ingress controller [install-ingress](https://kubernetes.github.io/ingress-nginx/deploy/#quick-start).

2. Apply the following yamls:
```bash
kubectl apply -f ./k8s/deployment.yaml
kubectl apply -f ./k8s/service.yaml
kubectl apply -f ./k8s/ingress.yaml

kubectl port-forward --namespace=ingress-nginx service/ingress-nginx-controller 8080:80
```
2. To connect k8s to consul and install node-exporter and filebeat. run jeknins job. 
    - jenkinsFiles/install_consul_k8s.groovy
    - jenkinsFiles/install_k8s_services.groovy
    - Go over jenkinsFiles/manual_steps.md

## Test web-api
I will use postman for api request.
1. Make POST request to "http://yaml-extract.test.localdev.me:8080//api/yaml_extract"
2. In the body of the request pass:
```bash
{
  "text": "root:\n    child1:\n        list:\n            - element1\n            - element2\n        listOfdicts:\n            - key1: element1\n              key2: element2\n    child2:\n        child2t: \"text\"",
  "expr": "root.child1.list[0]"
}
```