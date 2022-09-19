CREATE TABLE `scores` (
  `answer` varchar(6) NOT NULL,
  `guess` varchar(6) NOT NULL,
  `score` varchar(6) NOT NULL,
  PRIMARY KEY (`guess`,`answer`),
  KEY `guess` (`guess`,`score`),
  KEY `answer` (`answer`,`score`)
);

LOAD DATA LOCAL INFILE '../data/scores.txt' INTO TABLE `scores` FIELDS TERMINATED BY '|';

CREATE TABLE `all_scores` (
  `answer` varchar(6) NOT NULL,
  `guess` varchar(6) NOT NULL,
  `score` varchar(6) NOT NULL,
  PRIMARY KEY (`guess`,`answer`),
  KEY `guess` (`guess`,`score`),
  KEY `answer` (`answer`,`score`)
);

LOAD DATA LOCAL INFILE '../data/all-scores.txt' INTO TABLE `all_scores` FIELDS TERMINATED BY '|';

CREATE TABLE `answers` (
  `answer` varchar(6) NOT NULL PRIMARY KEY
);

INSERT INTO answers SELECT DISTINCT answer FROM scores;

CREATE TABLE `guesses` (
  `guess` varchar(6) NOT NULL PRIMARY KEY
);

insert into guesses select distinct guess from scores;

CREATE TABLE `all_guesses` (
  `guess` varchar(6) NOT NULL PRIMARY KEY
);

insert into all_guesses select distinct guess from all_scores;
