# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.fruit import Fruit  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_fruits_delete(self):
        """Test case for fruits_delete

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/q/openapi/fruits',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fruits_get(self):
        """Test case for fruits_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/q/openapi/fruits',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fruits_id_delete(self):
        """Test case for fruits_id_delete

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/q/openapi/fruits/{id}'.format(id='8dd6f91d-6378-4f52-b817-00cbc85ca39e'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fruits_id_get(self):
        """Test case for fruits_id_get

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/q/openapi/fruits/{id}'.format(id='8dd6f91d-6378-4f52-b817-00cbc85ca39e'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fruits_post(self):
        """Test case for fruits_post

        
        """
        fruit = {
  "name" : "lemon",
  "description" : "sour, yellow",
  "pick_date" : "2000-01-23T04:56:07.000+00:00",
  "weight" : 150,
  "id" : "8dd6f91d-6378-4f52-b817-00cbc85ca39e"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/q/openapi/fruits',
            method='POST',
            headers=headers,
            data=json.dumps(fruit),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
