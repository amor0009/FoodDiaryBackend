import logging
import redis.asyncio as aioredis
import json
from typing import Optional
from src.core.config import REDIS_URL

logger = logging.getLogger("food_diary_backend.cache")

class Cache:
    def __init__(self, redis_url: str = REDIS_URL):
        self.redis_url = redis_url
        self.pool: Optional[aioredis.Redis] = None

    async def connect(self):
        self.pool = await aioredis.from_url(self.redis_url, decode_responses=True)
        logger.info("Connected to Redis (cache)")

    async def get(self, key: str):
        try:
            logger.info(f"Попытка получения данных из кэша для ключа {key}")
            value = await self.pool.get(key)
            if value:
                logger.info(f"Данные успешно получены из кэша для ключа {key}")
                return json.loads(value)  # Десериализация строки JSON в объект Python
            else:
                logger.warning(f"Данные не найдены в кэше для ключа {key}")
                return None
        except Exception as e:
            logger.error(f"Ошибка при получении данных из кэша для ключа {key}: {str(e)}")
            raise e

    async def set(self, key: str, value, expire: int = 3600):
        try:
            logger.info(f"Добавление данных в кэш с ключом {key}")
            json_value = json.dumps(value)  # Сериализация объекта Python в строку JSON
            await self.pool.set(key, json_value, ex=expire)
            logger.info(f"Данные успешно добавлены в кэш с ключом {key}")
        except Exception as e:
            logger.error(f"Ошибка при добавлении данных в кэш с ключом {key}: {str(e)}")
            raise e

    async def delete(self, key: str):
        if self.pool:
            await self.pool.delete(key)
            logger.info(f"Кэш удален для ключа {key}")

    async def disconnect(self):
        if self.pool:
            await self.pool.close()
            logger.info("Disconnected from Redis (cache)")

cache = Cache()
