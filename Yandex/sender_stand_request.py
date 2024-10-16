import configuration
import requests
import data

def create_order():
    response_create_order = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=data.order_body,
                         headers=data.headers)
    return response_create_order.json()["track"]

def get_order(order_track):
    response_get_order = requests.get(configuration.URL_SERVICE + configuration.ORDERS_PATH + str(order_track))
    return response_get_order
