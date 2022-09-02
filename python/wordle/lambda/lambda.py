import json, sys
from Wordle import Wordle

def handler(event, context) :
    if 'body' in event:
        data = event['body']
        # deserialize if necessary
        if type(data) is str:
            data = json.loads(data)
            
        

        output = "operation not supported"
        hard_mode = False
        if 'hard_mode' in data:
            hard_mode = True

        sqlite_dbname = "/mnt/efs/wordle.sqlite"
        if 'sqlite_dbname' in data:
            sqlite_dbname = data['sqlite_dbname']

        if data['operation'] == "remaining_answers":
            wordle = Wordle(sqlite_dbname = sqlite_dbname,
                            hard_mode = hard_mode,
                            guess_scores = data['guess_scores'])
            output = wordle.remaining_answers()

        if data['operation'] == "guess":
            wordle = Wordle(sqlite_dbname = sqlite_dbname,
                            hard_mode = hard_mode,
                            guess_scores = data['guess_scores'])
            output = wordle.guess()

        if data['operation'] == "solve":
            start_with = []
            if 'start_with' in data:
                start_with = data['start_with']
            wordle = Wordle(sqlite_dbname = sqlite_dbname,
                            guess_scores = [],
                            hard_mode = hard_mode)
            output = wordle.solve(data['target'], start_with=start_with)

        headers = {
            "Access-Control-Allow-Headers": 
            "Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Origin": "https://dict.ramakocherlakota.net"
        };
        return {
            "headers": headers,
            "statusCode": 200,
            "body": json.dumps(
                output
            )
        }


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        data = json.load(file)
        print(handler({"body": data}, None))
