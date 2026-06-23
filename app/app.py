import time
import random
from flask import Flask
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST

app= Flask(__name__)

REQUEST_COUNT = Counter(
    'app_requests_total',   #metric name(How its shown in prometheus)
    'Total number of requests',     #human description
    ['endpoint']                #label:lets you filter by endpoint
)

ACTIVE_USERS = Gauge(
    'app_active_users',
    'simulated number of active users'
)

RESPONSE_TIME = Gauge(
    'app_response_time_seconds',
    "Simulated response time in seconds"
)

def simulate_metrics():
    #Update gauges with random values to simulate a live application
    ACTIVE_USERS.set(random.randint(10, 500))
    RESPONSE_TIME.set(round(random.uniform(0.1, 2.5), 3))

#ROUTES

@app.route('/')
def home():
    REQUEST_COUNT.labels(endpoint='/').inc() #increment counter for this endpoint
    simulate_metrics()
    return "Monitoring app is running. Visit /metrics to see Prometheus data."

@app.route('/api/data')
def data():
    REQUEST_COUNT.labels(endpoint='/api/data').inc() #increment counter for this endpoint
    simulate_metrics()
    return {"status":"ok" , "message":"data endpoint hit"}

@app.route('/metrics')
def metrics():
    #generate_lates() formats all your metrics into Prometheus text format
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000)