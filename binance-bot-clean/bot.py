from binance.client import Client

class BasicBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='MARKET',
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='LIMIT',
                    timeInForce='GTC',
                    quantity=quantity,
                    price=price
                )
            return order
        except Exception as e:
            return {"error": str(e)}
    



    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='STOP_MARKET',
                quantity=quantity,
                stopPrice=stop_price,
                price=limit_price,
                timeInForce='GTC',
                workingType='CONTRACT_PRICE'
            )
            return order
        except Exception as e:
            return {"error": str(e)}
    


    def get_open_orders(self, symbol=None):
        try:
            if symbol:
                return self.client.futures_get_open_orders(symbol=symbol)
            return self.client.futures_get_open_orders()
        except Exception as e:
            return {"error": str(e)}


