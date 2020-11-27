import pymemcache
import logging


# Configure logger
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger()

# Configure memcached
memcached_host = "memcached-cluster.2mgebk.cfg.use2.cache.amazonaws.com"
memcached_port = 11211


def connect_and_set():
    logger.info("[connect_and_set] Connecting to elasticache...")
    client = pymemcache.client.base.Client((memcached_host, memcached_port))

    logger.info("[connect_and_set] Setting some_key...")
    client.set('some_key', 'some value')

    logger.info("[connect_and_set] Getting some_key...")
    result = client.get('some_key')
    logger.info("[connect_and_set] Got some key %s", result)
