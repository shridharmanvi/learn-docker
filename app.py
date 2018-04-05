from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    return "Hey there!!! How you doin?"

@app.route('/hitme', methods=['GET'])
def hitme():
    print 'Here'
    return "I have been hit {} times!".format(get_hit_count())

@app.route('/myroute', methods=['GET'])
def myroute():
    return "Just testing another route!"

def get_hit_count():
    try:
        return cache.incr('hit_count')
    except redis.exceptions.ConnectionError:
        return 0

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
