from contextlib import closing
import sqlite3, sys, gzip, math

dbname = sys.argv[1]
file = sys.argv[2]

with closing(sqlite3.connect(dbname)) as connection:
    cursor = connection.cursor()
    cursor.execute("create table scores(answer text, guess text, score text)")
    cursor.execute("create unique index idx_scores_guess_answer on scores(guess, answer)")
    cursor.execute("create index idx_scores_guess_score on scores(guess, score)")

    fh = None
    if file.endswith(".gz"):
        fh = gzip.open(file, "rt")
    else:
        fh = open(file)
    
    n = 0
    while True:
        line = fh.readline()
#        print(line.rstrip())
        if line :
            [answer, guess, score] = line.rstrip().split("|")
            cursor.execute(f"insert into scores(answer, guess, score) values('{answer}', '{guess}', '{score}')")
            n = n + 1
            if n % 1000 == 0:
                print(n)
                connection.commit()
        else :
            break

    cursor.execute("create table answers(answer text not null primary key)");
    cursor.execute("insert into answers select distinct answer from scores")

    cursor.execute("create table guesses(guess text not null primary key)");
    cursor.execute("insert into guesses select distinct guess from scores")

    cursor.execute("create table log2_lookup(n int not null primary key, log2n float not null)")
    for n in range(1, 10000):
        cursor.execute(f"insert into log2_lookup(n, log2n) values({n}, {math.log(n, 2)})")

    connection.commit()
