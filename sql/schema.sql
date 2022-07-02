CREATE TABLE `scores` (
  `answer` varchar(6) NOT NULL,
  `guess` varchar(6) NOT NULL,
  `score` varchar(6) NOT NULL,
  PRIMARY KEY (`guess`,`answer`),
  KEY `guess` (`guess`,`score`),
  KEY `answer` (`answer`,`score`)
);

LOAD DATA LOCAL INFILE '../data/scores.txt' INTO TABLE `scores`;

CREATE TABLE `answers` (
  `answer` varchar(6) NOT NULL PRIMARY KEY
);

LOAD DATA LOCAL INFILE '../data/answers.txt' INTO TABLE `answers`;

