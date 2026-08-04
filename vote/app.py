from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def vote():
    r.incr('cats')
    return "Vote Recorded"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
