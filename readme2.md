### Commands to set up the db

sudo -i -u postgres
createdb database_name
createuser name_of_user_to_administer_db

psql
grant all privileges on database database_name to name_of_user_to_administer_db;
alter user app with encrypted password 'a pretty good password';

### Commands to interact with db

flask db-custom drop drops the database
flask db upgrade resets the database with the most recent migrations
flask db-custom seed seeds the database

| Command                   | Effect                                              |
| ------------------------- | --------------------------------------------------- |
| flask db-custom drop      | drops the database                                  |
| flask db upgrade          | resets the database with the most recent migrations |
| flask db-custom seed      | seeds the database                                  |
| flask db-custom downgrade | rolls back the database                             |

This project contains the following pip packages
NB This does not include their dependencies. Please see the requirements.txt

| package                | Use                                                      |
| ---------------------- | -------------------------------------------------------- |
| bcrypt                 | Good password hashing for your software and your servers |
| boto3                  | AWS python SDK                                           |
| Flask                  | Python Micro Framework                                   |
| Flask-JWT-Extended     | Support for managing JWTs with flask                     |
| flask-marshmallow      | Integration layer for Flaks and Marshmallow              |
| marshmallow            | used to convert complex datatypes ,to and from Python    |
| Flask-Migrate          | xxxx                                                     |
| Flask-SQLAlchemy       | xxxx                                                     |
| marshmallow-sqlalchemy | xxxx                                                     |
| psycopg2-binary        | xxxx                                                     |
| SQLAlchemy             | xxxx                                                     |
