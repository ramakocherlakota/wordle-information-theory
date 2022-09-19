create table first_guess as select guess, sum(c * log(2, c)) / sum(c) as h from (select guess, score, count(*) as c from scores group by 1, 2 ) as t1 group by 1 ;

alter table first_guess add key(h);
alter table first_guess add key(guess, h);

create table first_guess_all as select guess, sum(c * log(2, c)) / sum(c) as h from (select guess, score, count(*) as c from all_scores group by 1, 2 ) as t1 group by 1 ;

alter table first_guess_all add key(h);
alter table first_guess_all add key(guess, h);
