--for PSQL database
create table users (
    id bigserial primary key,
    uid varchar(128) unique not null,
    user_name varchar(128) not null,
    role varchar(32) not null,
    is_verified boolean not null,
    registered_date timestamp
);