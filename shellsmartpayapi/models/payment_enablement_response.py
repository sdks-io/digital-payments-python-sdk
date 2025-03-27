# -*- coding: utf-8 -*-

"""
shellsmartpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PaymentEnablementResponse(object):

    """Implementation of the 'PaymentEnablementResponse' model.

    Attributes:
        dpan_last_4 (str): DPan Last number

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dpan_last_4": 'dpanLast4'
    }

    def __init__(self,
                 dpan_last_4=None):
        """Constructor for the PaymentEnablementResponse class"""

        # Initialize members of the class
        self.dpan_last_4 = dpan_last_4 

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
        dpan_last_4 = dictionary.get("dpanLast4") if dictionary.get("dpanLast4") else None
        # Return an object of this model
        return cls(dpan_last_4)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'dpan_last_4={self.dpan_last_4!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'dpan_last_4={self.dpan_last_4!s})')
