import redis
import time

redis_client = redis.StrictRedis(host="redis", port=6379, decode_responses=True)
worker_name = "Worker1"  
while True:
    task = redis_client.blpop("task_queue", timeout=5)  
    if task:
        print(f"{worker_name} processed: {task[1]}")
        time.sleep(2)  
    else:
        print(f"{worker_name} waiting for tasks...")

