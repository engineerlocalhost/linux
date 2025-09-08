#Installing ONLYOFFICE Workspace using Docker Compose
apt install docker.io #install docker
apt-get install docker-compose-plugin #install docker compose
git clone https://github.com/ONLYOFFICE/Docker-CommunityServer
cd Docker-CommunityServer
    docker-compose.groups.yml for Community Server (distributed as ONLYOFFICE Groups)
    docker-compose.workspace.yml for ONLYOFFICE Workspace Community Edition
    docker-compose.workspace_enterprise.yml for ONLYOFFICE Workspace Enterprise Edition
docker compose -f docker-compose.workspace.yml up -d 