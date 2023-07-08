from aiohttp import ClientSession, ClientResponse
from decimal  import Decimal
BINANCE_URL = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"
HUOBI_URL = "https://api.huobi.pro/market/detail/merged?symbol=btcusdt"
OKX_URL = "https://www.okex.com/api/v5/market/ticker?instId=BTC-USDT"


async def fetch_data_binance(session: ClientSession) -> float:
    url = BINANCE_URL
    async with session.get(url) as result:
        binance_ticker_data = await result.json()
        best_bid = binance_ticker_data.get("bidPrice")
        best_ask = binance_ticker_data.get("askPrice")
        best_bid = float(Decimal(best_bid))
        best_ask = float(Decimal(best_ask))
        mid_price = float(Decimal(best_bid) + Decimal(best_ask)) / 2
        return mid_price


async def fetch_data_okx(session: ClientSession) -> float:
    url = OKX_URL
    async with session.get(url) as result:
        okx_ticker_data = await result.json()
        best_bid = okx_ticker_data.get("data")[0].get("bidPx")
        best_ask = okx_ticker_data.get("data")[0].get("askPx")
        best_bid = float(Decimal(best_bid))
        best_ask = float(Decimal(best_ask))
        mid_price = float(Decimal(best_bid / 2) + Decimal(best_ask / 2))
        return mid_price


async def fetch_data_huobi(session: ClientSession) -> float:
    url = HUOBI_URL
    async with session.get(url) as result:
        huobi_ticker_data = await result.json()
        best_bid = huobi_ticker_data.get("tick").get("bid")[0]
        best_ask = huobi_ticker_data.get("tick").get("ask")[0]
        best_bid = float(Decimal(best_bid))
        best_ask = float(Decimal(best_ask))
        mid_price = float(Decimal(best_bid / 2) + Decimal(best_ask / 2))
        return mid_price
