import json
from Wordle import Wordle

def handler(event, context) :
    print("event=")
    print(event)
    if 'body' in event:
        data = event['body']
        print("data=")
        print(data)
        # deserialize if necessary
        if type(data) is str:
            data = json.loads(data)
            print("after loads, data=")
            print(data)
            
        wordle = Wordle(sqlite_dbname = "wordle.sqlite",
                        sqlite_bucket = "wordle-sqlite",
                        guess_scores = data['guess_scores'])
        guess =  wordle.guess()

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
                guess
            )
        }


if __name__ == "__main__":
    with open("/Users/rama/tmp/guess.json") as file:
        event = json.load(file)
        print(handler(event, None))
