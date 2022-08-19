while read -r target;
do
    echo $target
    echo "  `date`"    
    python solve.py --start=raise $target | jq . > ./experiments/raise-not-hard/$target.json
    python solve.py --start=raise --hard $target | jq . > ./experiments/raise-hard/$target.json
    python solve.py --start=salon,trice $target | jq . > ./experiments/trice-salon-not-hard/$target.json
    python solve.py --start=salon,trice --hard $target | jq . > ./experiments/trice-salon-hard/$target.json
    echo "  `date`"    
done 
