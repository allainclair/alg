import json
from urllib import request
from urllib.error import (URLError)

from conf import ENDPOINT_PRODUCTS


def get_products(endpoint=ENDPOINT_PRODUCTS):
    try:
        resource = request.urlopen(endpoint)
        resource_body = resource.read()
        json_object = json.loads(resource_body.decode("utf-8"))
        return json_object['products']
    except URLError as exc:
        raise Warning(f"Could not get Products from '{ENDPOINT_PRODUCTS}'") from exc
