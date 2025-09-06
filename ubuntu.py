#Setelah install Ubuntu Desktop

#change password root
sudo passwd root #masukan password root

#update & Upgrade
apt update && apt upgrade -y

#Installasi Apps pendukung
apt install git #install git
dpkg -i #install .*deb apps
apt install golang-go #install golang
    go version #check golang versi
install gnome-tweaks #tweaks gnome

================================================

#Installing ONLYOFFICE Workspace using Docker Compose
apt install docker.io #install docker
apt-get install docker-compose-plugin #install docker compose
git clone https://github.com/ONLYOFFICE/Docker-CommunityServer
cd Docker-CommunityServer
    docker-compose.groups.yml for Community Server (distributed as ONLYOFFICE Groups)
    docker-compose.workspace.yml for ONLYOFFICE Workspace Community Edition
    docker-compose.workspace_enterprise.yml for ONLYOFFICE Workspace Enterprise Edition
docker compose -f docker-compose.workspace.yml up -d 

email   : engineerlocalhost@gmail.com
User    : Administrator
Passwd  : Sayasaja007
==================================================