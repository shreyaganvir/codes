# Pre-requisites
# make necessary variable updates in .env and docker-compose.yml files. login to docker.io with docker hub credentials

# Docker Build
docker build --file Dockerfile  --tag "<dockerhub_username>/minirest_app:latest_1>" .

# Docker Tag
docker tag "<dockerhub_username>/minirest_app:test" "<dockerhub_username>/minirest_app:latest"

# Docker run locally
# docker compose up -d minirest_db
# sleep(10)
# docker compose up -d minirest_app

# Docker push
docker push "<dockerhub_username>/minirest_app:latest_1"