# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class OauthTokenPostRequestBody(object):

    """Implementation of the 'oauthTokenPostRequestBody' model.

    TODO: type model description here.

    Attributes:
        grant_type (str): In OAuth 2.0, the term grant typee refers to the way
            an application gets an access token. OAuth 2.0 defines several
            grant types, including the authorization code flow.
        client_id (str): After registering your app, you will receive a client
            ID and a client secret. The client ID is considered public
            information, and is used to build login URLs, or included in
            Javascript source code on a page.
        client_secret (str): After registering your app, you will receive a
            client ID and a client secret. The client ID is considered public
            information, and is used to build login URLs, or included in
            Javascript source code on a page. The client secret must be kept
            confidential.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "grant_type": 'grant_type',
        "client_id": 'client_id',
        "client_secret": 'client_secret'
    }

    def __init__(self,
                 grant_type='client_credentials',
                 client_id='SOFflRakNlwnWlxfOXQ4GHDVyqGawuKA',
                 client_secret='cRnWgw7gACqM3gVS'):
        """Constructor for the OauthTokenPostRequestBody class"""

        # Initialize members of the class
        self.grant_type = grant_type 
        self.client_id = client_id 
        self.client_secret = client_secret 

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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        grant_type = dictionary.get("grant_type") if dictionary.get("grant_type") else 'client_credentials'
        client_id = dictionary.get("client_id") if dictionary.get("client_id") else 'SOFflRakNlwnWlxfOXQ4GHDVyqGawuKA'
        client_secret = dictionary.get("client_secret") if dictionary.get("client_secret") else 'cRnWgw7gACqM3gVS'
        # Return an object of this model
        return cls(grant_type,
                   client_id,
                   client_secret)
