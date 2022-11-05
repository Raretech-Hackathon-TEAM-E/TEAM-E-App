CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
USE chatapp
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser'@'localhost';

CREATE TABLE users (
    uid varchar(255) PRIMARY KEY,
    user_name varchar(255) UNIQUE NOT NULL,
    email varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL,
    u_intro varchar(255) NULL,
    u_signup_time timestamp NOT NULL default current_timestamp,
    u_update_time timestamp NULL
);

CREATE TABLE channels (
    cid serial PRIMARY KEY,
    channel_name varchar(255) UNIQUE NOT NULL,
    uid varchar(255) REFERENCES users(uid),
    abstract varchar(255) NOT NULL,
    c_add_time timestamp NOT NULL default current_timestamp,
    c_update_time timestamp NULL
);

CREATE TABLE messages (
    mid serial PRIMARY KEY,
    uid varchar(255) REFERENCES users(uid),
    cid integer REFERENCES channels(cid) ON DELETE CASCADE,
    message text,
    m_add_time timestamp NOT NULL default current_timestamp,
    quote_mid bigint unsigned UNIQUE NULL
);