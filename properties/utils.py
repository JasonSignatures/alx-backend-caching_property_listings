# properties/utils.py

import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)


def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and calculate hit ratio.
    """
    redis_conn = get_redis_connection("default")
    info = redis_conn.info()

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)

    total = hits + misses
    hit_ratio = hits / total if total > 0 else 0

    metrics = {
        "keyspace_hits": hits,
        "keyspace_misses": misses,
        "hit_ratio": hit_ratio,
    }

    logger.info(
        "Redis Cache Metrics | Hits: %s | Misses: %s | Hit Ratio: %.2f",
        hits,
        misses,
        hit_ratio,
    )

    return metrics
