CREATE TABLE googleplaystore (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    rating FLOAT,
    reviews INTEGER,
    size VARCHAR(255),
    installs VARCHAR(255),
    type VARCHAR(255),
    price VARCHAR(255),
    content_rating VARCHAR(255),
    genres VARCHAR(255),
    last_update VARCHAR(255),
    current_ver VARCHAR(255),
    android_ver VARCHAR(255),
);
CREATE TABLE googleplaystore_user_reviews(
    id SERIAL PRIMARY KEY,
    app_name VARCHAR(255),
    translated_review VARCHAR(255),
    sentiment VARCHAR(255),
    sentiment_Polarity FLOAT,
    sentiment_subjectivity FLOAT;
);

COPY googleplaystore
FROM '/var/lib/postgresql/data/googleplaystore.csv'
DELIMITER ','
CSV HEADER;

COPY googleplaystore_user_reviews
FROM '/var/lib/postgresql/data/googleplaystore_user_reviews.csv'
DELIMITER ','
CSV HEADER;