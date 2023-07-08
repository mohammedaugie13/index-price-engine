from aioshutdown import SIGTERM, SIGINT, SIGHUP
from index_price_engine.fetcher import watcher


def cli():
    with SIGTERM | SIGHUP | SIGINT as loop:
        loop.create_task(watcher())
        loop.run_forever()
