# -*- coding: utf-8 -*-

"""
shellsmartpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from shellsmartpayapi.api_helper import APIHelper
from shellsmartpayapi.exceptions.api_exception import APIException
from shellsmartpayapi.models.mpp_error import MppError


class CancelFuelingErrorResponseErrorException(APIException):
    def __init__(self, reason, response):
        """Constructor for the CancelFuelingErrorResponseErrorException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(CancelFuelingErrorResponseErrorException, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.error_code = dictionary.get("errorCode") if dictionary.get("errorCode") else None
        self.error_description = dictionary.get("errorDescription") if dictionary.get("errorDescription") else None
        self.errors = None
        if dictionary.get('errors') is not None:
            self.errors = [MppError.from_dictionary(x) for x in dictionary.get('errors')]
        else:
            self.errors = None

    def __str__(self):
        base_str = super().__str__()
        return (f'{self.__class__.__name__}('
                f'{base_str[base_str.find("(") + 1:-1]}, '
                f'error_code={(self.error_code if hasattr(self, "error_code") else None)!s}, '
                f'error_description={(self.error_description if hasattr(self, "error_description") else None)!s}, '
                f'errors={(self.errors if hasattr(self, "errors") else None)!s})')
