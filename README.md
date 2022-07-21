### Start the Docker container of Postgres

```
docker-compose build
docker-compose up db
```
### Connect to the container filesystem

Open a new Terminal and connect to the system of the Docker
`docker exec -it DOCKER_ID bash`

In order to get the DOCKER_ID you need to run `docker ps` 

Now you are connected to the system of the Postgres container, which is a Debian OS.

The Postgres is installed at `/var/lib/postgresql`

### Install pgloader

In order to install the `pgloader`inside the container: 

```
apt-get update
apt-get install pgloader
```
If more Debian tools are missing, you can install them the same way.

### Copy the database file to the container

Then you want to pass the `amadeus4dev.db` to the Docker. In order to do so from a terminal of your localhost:
One specific file can be copied TO the container like:

```
docker cp amadeus4dev.db DOCKER_ID:/amadeus4dev.db
```

### Migrate the database with one line command

```
createdb -U user newdb
pgloader -d -U user amadeus4dev.db postgresql:///newdb
```

### Migrate the database with the load script 

Create a file `config.load`
```
load database
     from sqlite:amadeus4dev.db
     into postgresql:///pdb

 with include drop, create tables, create indexes, reset sequences

  set work_mem to '16MB', maintenance_work_mem to '512 MB';

```
Run it with 

```
pgloader -d -U user config.load 
```

### Run queries to the database

```sql
psql -U user -d newdb -c "SELECT * FROM information_schema.tables"
psql -U user -d newdb -c "SELECT * FROM users"
```