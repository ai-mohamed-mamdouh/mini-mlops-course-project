import redis

class RedisClient:

    def __init__(
        self,
        host: str,
        port: int
    ):
        self.client = redis.Redis(
            host=host,
            port=port,
            db=1,
            decode_responses=True
        )

    def set(
        self,
        key,
        value,
        expire=None
    ):
        return self.client.set(
            key,
            value,
            ex=expire
        )

    def get(self, key):
        return self.client.get(key)

    def exists(self, key):
        return self.client.exists(key)

    def delete(self, key):
        return self.client.delete(key)