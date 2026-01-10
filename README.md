# the-closet
Application that gives user apparel recommendations based on their skin tone and body type. Work in progress...

## Starting the flask server
Once at the root directory, open powershell/bash terminal and run the following commands:

#### Windows
```
cd <root_directory>
.venv\Scripts\activate
waitress-serve --listen=<IP>:<port> --call 'app:create_app'
```

This will spin up the flask server which responds to the request coming through the defined 'port'. We are still needed to initialize the DB separately, which is being covered in the following section. 

## Initializing SQLite DB 
In order to start the DB, open powershell/bash. Get to the project's directory and run following commands:

```
flask --app app init-db
```

This will prompt the message "Initialized the database" and will instantiate a SQLite DB. Everytime flask app is launched either by using gunicorn(linux/MacOS) or waitress(Windows), all the tables will be dropped and the same tables will be re-instantiated. Empty each time.

Once the SQLite DB is initialized, we would be able to see it's instance being created at 'instance/closet-users-db.sqlite' at the root app directory
