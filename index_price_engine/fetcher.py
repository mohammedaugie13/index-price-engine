import asyncio
import aiohttp
from index_price_engine.utils import fetch_data_okx, fetch_data_huobi, fetch_data_binance
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


async def watcher():
    try:
        while True:
            await asyncio.sleep(10)
            prices = []
            async with aiohttp.ClientSession() as session:
                fetchers = [
                    asyncio.create_task(fetch_data_huobi(session)),
                    asyncio.create_task(fetch_data_binance(session)),
                    asyncio.create_task(fetch_data_okx(session)),
                ]

                done, pending = await asyncio.wait(fetchers)

                for done_task in done:
                    if done_task.exception() is None:
                        prices.append(done_task.result())
                    else:
                        logging.error("ERROR")

            logging.info(f"INDEX PRICE BTC USDT {sum(prices)/3}")
    except asyncio.CancelledError as exc:
        # Received an exit signal. In this place we gracefully complete the work.
        signal = exc.args[0] # NOTE: works in Python >= 3.9 only: https://docs.python.org/3/library/asyncio-future.html?highlight=Changed%20in%20version%203.9:%20Added%20the%20msg%20parameter.#asyncio.Future.cancel
        logging.warning("Received %s signal. Shutting down...", signal.value)



