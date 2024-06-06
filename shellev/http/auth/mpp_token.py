# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.header_auth import HeaderAuth


class MppToken(HeaderAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in MppToken

        """
        return "MppToken: Authorization is undefined."

    def __init__(self, mpp_token_credentials):
        auth_params = {}
        if mpp_token_credentials is not None \
                and mpp_token_credentials.authorization is not None:
            auth_params["Authorization"] = mpp_token_credentials.authorization
        super().__init__(auth_params=auth_params)


class MppTokenCredentials:

    @property
    def authorization(self):
        return self._authorization

    def __init__(self, authorization):
        if authorization is None:
            raise ValueError('authorization cannot be None')
        self._authorization = authorization

    def clone_with(self, authorization=None):
        return MppTokenCredentials(authorization or self.authorization)
