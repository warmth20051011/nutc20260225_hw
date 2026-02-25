import os

SECRET_KEY = "enterprise_secret"
ALGORITHM = "HS256"

REDIS_HOST = "localhost"
REDIS_PORT = 6379

LITELLM_URL = "http://localhost:4000/v1/chat/completions"

RATE_LIMIT_PER_MINUTE = 30
