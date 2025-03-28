# -*- coding: utf-8 -*-

"""
shellsmartpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CollectingCompany(object):

    """Implementation of the 'CollectingCompany' model.

    Attributes:
        col_co_id (str): The ID of the Collecting Company (in GFN), also known
            as Shell Code of the selected payer. This property is mandatory if
            the ColCoCode code is not passed

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_id": 'ColCoId'
    }

    def __init__(self,
                 col_co_id=None):
        """Constructor for the CollectingCompany class"""

        # Initialize members of the class
        self.col_co_id = col_co_id 

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
        col_co_id = dictionary.get("ColCoId") if dictionary.get("ColCoId") else None
        # Return an object of this model
        return cls(col_co_id)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={self.col_co_id!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={self.col_co_id!s})')
