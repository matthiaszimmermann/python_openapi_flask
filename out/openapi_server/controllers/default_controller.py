import connexion
import six
import uuid

from openapi_server.models.fruit import Fruit  # noqa: E501
from openapi_server import util

fruit_basket = {}

def fruits_delete():  # noqa: E501
    """fruits_delete

    Delete all fruits # noqa: E501


    :rtype: None
    """

    fruit_basket = {}

    return None, 200


def fruits_fruit_id_delete(fruit_id):  # noqa: E501
    """fruits_fruit_id_delete

    Delete the fruit with the specified id # noqa: E501

    :param id: A resource identifier
    :type id: 

    :rtype: None
    """
    try:
        fruit_basket.pop(fruit_id, None)
        response = fruit_id, 200
    except KeyError:
        response = {}, 404

    return response

def fruits_fruit_id_get(fruit_id):  # noqa: E501
    """fruits_fruit_id_get

    Get a single fruit # noqa: E501

    :param id: A resource identifier
    :type id: 

    :rtype: Fruit
    """
    try:
        fruit = fruit_basket[fruit_id]
        response = fruit, 200
    except KeyError:
        response = {}, 404

    return response


def fruits_get():  # noqa: E501
    """fruits_get

    List all fruits # noqa: E501


    :rtype: List[Fruit]
    """
    return list(fruit_basket.values())


def fruits_post(fruit=None):  # noqa: E501
    """fruits_post

    Create this fruit as a resource # noqa: E501

    :param fruit: 
    :type fruit: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        fruit = Fruit.from_dict(connexion.request.get_json())  # noqa: E501
        id = fruit.id

        if(id is None or len(id) == 0):
            id = str(uuid.uuid4())
            fruit.id = id

        fruit_basket[id] = fruit
    
    return fruit, 200
