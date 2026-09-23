import json
import hashlib

class RedisService:
    """
    Service layer for ML prediction caching using Redis.
    """

    def __init__(self, redis_client):
        self.redis_client = redis_client


    def _generate_key(self, features):
        """
        Generate unique key from input features.
        """

        features_string = json.dumps(
            features,
            sort_keys=True
        )

        feature_hash = hashlib.md5(
            features_string.encode()
        ).hexdigest()

        return f"prediction:{feature_hash}"


    def get_prediction(self, features):
        """
        Retrieve cached prediction if exists.
        """

        key = self._generate_key(features)

        result = self.redis_client.get(key)

        if result:
            return json.loads(result)

        return None


    def save_prediction(
        self,
        features,
        prediction,
        expire: int = 3600
    ):
        """
        Save prediction result in cache.
        """

        key = self._generate_key(features)

        self.redis_client.set(
            key,
            json.dumps(prediction),
            expire
        )


    def delete_prediction(self, features):
        """
        Delete cached prediction.
        """

        key = self._generate_key(features)

        return self.redis_client.delete(key)