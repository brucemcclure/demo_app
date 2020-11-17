### Commands to set up the db

sudo -i -u postgres
createdb database_name
createuser name_of_user_to_administer_db

psql
grant all privileges on database database_name to name_of_user_to_administer_db;
alter user app with encrypted password 'a pretty good password';
