import os

SECRET_KEY = os.getenv("SECRET_KEY", "enterprise_secret")
ALGORITHM = "HS256"

REDIS_HOST = "redis"
REDIS_PORT = 6379

LITELLM_URL = "http://litellm:4000/v1/chat/completions"

RATE_LIMIT_PER_MINUTE = 30
