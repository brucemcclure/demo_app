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
