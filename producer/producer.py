import redis
import time
import random

redis_client = redis.StrictRedis(host="redis", port=6379, decode_responses=True)
task_id = 1
while True:
    task = f"Task-{task_id}"
    redis_client.rpush("task_queue", task)
    print(f"Produced: {task}")
    task_id += 1
    time.sleep(random.randint(1, 3))
