# -*- coding: utf-8 -*-

"""
shellsmartpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellsmartpayapi.api_helper import APIHelper


class CancelFuelingRequest(object):

    """Implementation of the 'cancelFuelingRequest' model.

    Attributes:
        mpp_transaction_id (str): The model property of type str.
        reason_code (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mpp_transaction_id": 'mppTransactionId',
        "reason_code": 'reasonCode'
    }

    _optionals = [
        'mpp_transaction_id',
        'reason_code',
    ]

    def __init__(self,
                 mpp_transaction_id=APIHelper.SKIP,
                 reason_code=APIHelper.SKIP):
        """Constructor for the CancelFuelingRequest class"""

        # Initialize members of the class
        if mpp_transaction_id is not APIHelper.SKIP:
            self.mpp_transaction_id = mpp_transaction_id 
        if reason_code is not APIHelper.SKIP:
            self.reason_code = reason_code 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        mpp_transaction_id = dictionary.get("mppTransactionId") if dictionary.get("mppTransactionId") else APIHelper.SKIP
        reason_code = dictionary.get("reasonCode") if dictionary.get("reasonCode") else APIHelper.SKIP
        # Return an object of this model
        return cls(mpp_transaction_id,
                   reason_code)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'mpp_transaction_id={(self.mpp_transaction_id if hasattr(self, "mpp_transaction_id") else None)!r}, '
                f'reason_code={(self.reason_code if hasattr(self, "reason_code") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'mpp_transaction_id={(self.mpp_transaction_id if hasattr(self, "mpp_transaction_id") else None)!s}, '
                f'reason_code={(self.reason_code if hasattr(self, "reason_code") else None)!s})')
