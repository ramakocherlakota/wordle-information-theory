while read -r word;
do
    echo "$word,`cat raise-hard/$word.json | jq last.turn`,`cat raise-not-hard/$word.json | jq last.turn`,`cat trice-salon-hard/$word.json | jq last.turn`,`cat trice-salon-not-hard/$word.json | jq last.turn`" 
done  \
    > results.csv
