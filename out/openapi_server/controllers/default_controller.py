import connexion
import six

from openapi_server.models.bad_request_error import BadRequestError  # noqa: E501
from openapi_server.models.fruit import Fruit  # noqa: E501
from openapi_server.models.fruit_id import FruitId  # noqa: E501
from openapi_server.models.not_found_error import NotFoundError  # noqa: E501
from openapi_server import util


def fruits_delete():  # noqa: E501
    """fruits_delete

    Delete all fruits # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def fruits_fruit_id_delete(fruit_id):  # noqa: E501
    """fruits_fruit_id_delete

    Delete the fruit with the specified id # noqa: E501

    :param fruit_id: A resource identifier
    :type fruit_id: 

    :rtype: None
    """
    return 'do some magic!'


def fruits_fruit_id_get(fruit_id):  # noqa: E501
    """fruits_fruit_id_get

    Get a single fruit # noqa: E501

    :param fruit_id: A resource identifier
    :type fruit_id: 

    :rtype: Fruit
    """
    return 'do some magic!'


def fruits_fruit_id_patch(fruit_id):  # noqa: E501
    """fruits_fruit_id_patch

    Update the fruit with the specified id # noqa: E501

    :param fruit_id: A resource identifier
    :type fruit_id: 

    :rtype: None
    """
    return 'do some magic!'


def fruits_get():  # noqa: E501
    """fruits_get

    List all fruits # noqa: E501


    :rtype: List[Fruit]
    """
    
    for item in connexion.request.__dict__.items():
        print(item)

    host = get_host(connexion.request)
    tenant = get_tenant(connexion.request)
    version = get_version(connexion.request)

    print("host: {}, tenant: {}, version: {}".format(host, tenant, version))
    
    return 'do some magic!'

def get_version(request):
    rd = request.__dict__
    
    if 'path' in rd.keys():
        path = rd['path']

        if path.startswith('/api/v'):
            return path.split('/')[2]
        
    return None

def get_tenant(request):
    host = get_host(request)

    if host and '.' in host:
        return host.split('.')[0]
    
    return None

def get_host(request):
    rd = request.__dict__
    
    if 'host' in rd.keys():
        return rd['host']
    
    return None

def fruits_post(fruit=None):  # noqa: E501
    """fruits_post

    Create this fruit as a resource # noqa: E501

    :param fruit: 
    :type fruit: dict | bytes

    :rtype: FruitId
    """
    if connexion.request.is_json:
        fruit = Fruit.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
