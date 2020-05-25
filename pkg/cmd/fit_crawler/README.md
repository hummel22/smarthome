
# Crawler application that is run in a docker container to crawl owm for humidity and temperate readings
### Deploying

 - Update the .env file with new version
 -  `./dcoker-build.sh`
 - run `./dcoker-push` to push to aws repo
 - copy `docker-compose-server.yaml` and add city name
 - edit `./docker-deploy-server.sh` with new yaml file with proper city name
 - `./docker-deploy-server.sh`

### Adding a new city

Add a new object in the objects.Location package
The city can be called by the given name using the `LOCATION` para in docker compose

###Changelog

#### 1.0.1
 - Add Austin options
 - Create DC/Austin docker-compose files
 - Create README
 
#### 1.0
 - Record DC weather