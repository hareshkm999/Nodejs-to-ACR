docker build . -t fastapi-cd:1.0
docker images

docker run -p 8000:8000 -t fastapi-cd:1.0

## Infrastructure setup

## Azure Container Registry, create an Azure Container Registry.


az login
az acr login --name fastapicd777

## Build and push your Docker image to the registry server.
docker build . -t fastapicd777.azurecr.io/fastapi-cd:1.0
docker images
docker push fastapicd777.azurecr.io/fastapi-cd:1.0

## Azure App Service

App Service --> create --> 