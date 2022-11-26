DROP DATABASE chatapp;
DROP USER 'testuser'@'localhost';

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
    quote_mid bigint unsigned NULL,
    repostmark boolean
);

/* ユーザーネーム：test　パスワード：testpass */
INSERT INTO users(uid, user_name, email, password, u_signup_time) VALUES('7bf934b7-8a22-4bfd-832b-fe68fb29c76f', 'test', 'test@gmail.com', '13d249f2cb4127b40cfa757866850278793f814ded3c587fe5889e889a7a9f6c', '2022-11-08 0:20:20');
INSERT INTO channels(cid, channel_name, uid, abstract, c_add_time) VALUES('1', 'testchannel', '7bf934b7-8a22-4bfd-832b-fe68fb29c76f', 'testabstract', '2022-11-09 0:20:20');
INSERT INTO messages(mid, uid, cid, message, m_add_time) VALUES('1','7bf934b7-8a22-4bfd-832b-fe68fb29c76f', '1', 'This is a test message!', '2022-11-10 0:20:20');
INSERT INTO messages(mid, uid, cid, message, m_add_time, quote_mid, repostmark) VALUES('2', '7bf934b7-8a22-4bfd-832b-fe68fb29c76f', '1', 'I am repost.', '2022-11-11 0:20:20', '1', '1');

