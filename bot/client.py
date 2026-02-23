import requests
import time
import hmac
import hashlib
import logging

BASE_URL = "https://testnet.binancefuture.com"


class BinanceFuturesClient:
    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key

    def _sign(self, params: dict) -> str:
        query_string = "&".join([f"{k}={v}" for k, v in params.items()])
        signature = hmac.new(
            self.secret_key.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()
        return signature

    def place_order(self, params: dict) -> dict:
        endpoint = "/fapi/v1/order"

        params["timestamp"] = int(time.time() * 1000)
        params["recvWindow"] = 5000
        params["signature"] = self._sign(params)

        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        try:
            response = requests.post(
                BASE_URL + endpoint,
                headers=headers,
                params=params,
                timeout=10
            )

            logging.info(f"Request: {params}")
            logging.info(f"Response: {response.text}")

            if response.status_code != 200:
                print("Status Code:", response.status_code)
                print("Response Text:", response.text)
                response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            logging.error(f"API Error: {str(e)}")
            raise