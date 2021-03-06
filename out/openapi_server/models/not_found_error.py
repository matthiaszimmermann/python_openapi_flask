# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class NotFoundError(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, message=None):  # noqa: E501
        """NotFoundError - a model defined in OpenAPI

        :param id: The id of this NotFoundError.  # noqa: E501
        :type id: str
        :param message: The message of this NotFoundError.  # noqa: E501
        :type message: str
        """
        self.openapi_types = {
            'id': str,
            'message': str
        }

        self.attribute_map = {
            'id': 'id',
            'message': 'message'
        }

        self._id = id
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'NotFoundError':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NotFoundError of this NotFoundError.  # noqa: E501
        :rtype: NotFoundError
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this NotFoundError.

        The query ID  # noqa: E501

        :return: The id of this NotFoundError.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotFoundError.

        The query ID  # noqa: E501

        :param id: The id of this NotFoundError.
        :type id: str
        """

        self._id = id

    @property
    def message(self):
        """Gets the message of this NotFoundError.

        Human readable error message  # noqa: E501

        :return: The message of this NotFoundError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this NotFoundError.

        Human readable error message  # noqa: E501

        :param message: The message of this NotFoundError.
        :type message: str
        """

        self._message = message
