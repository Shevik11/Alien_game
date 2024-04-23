create database cosmic_game;
use cosmic_game;

CREATE TABLE score (
    top INT AUTO_INCREMENT PRIMARY KEY,
    score INT,
    max_score text
);


drop table score;