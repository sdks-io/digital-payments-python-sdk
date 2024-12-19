# -*- coding: utf-8 -*-

"""
shellsmartpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from shellsmartpayapi.api_helper import APIHelper
from shellsmartpayapi.configuration import Server
from shellsmartpayapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from shellsmartpayapi.http.http_method_enum import HttpMethodEnum
from shellsmartpayapi.models.access_token_response import AccessTokenResponse
from shellsmartpayapi.exceptions.access_token_error_exception import AccessTokenErrorException
from shellsmartpayapi.exceptions.api_exception import APIException


class PartnerNotificationController(BaseController):

    """A Controller to access Endpoints in the shellsmartpayapi API."""
    def __init__(self, config):
        super(PartnerNotificationController, self).__init__(config)

    def partner_token(self,
                      grant_type,
                      client_id,
                      client_secret):
        """Does a POST request to /token.

        To access the Partner’s endpoints, for sending callback messages,
        Shell will need to connect to the Partner API end points. It is
        recemmended that the partner offers OAuth 2.0 as a standard for call
        back APIs and will require the OAuth 2.0 token for authentication.
        Note this needs to be implemented over HTTPS

        Args:
            grant_type (str): In OAuth 2.0, the term grant typee refers to the
                way an application gets an access token. OAuth 2.0 defines
                several grant types, including the authorization code flow.
            client_id (str): After registering your app, you will receive a
                client ID and a client secret. The client ID is considered
                public information, and is used to build login URLs, or
                included in Javascript source code on a page.
            client_secret (str): After registering your app, you will receive
                a client ID and a client secret. The client ID is considered
                public information, and is used to build login URLs, or
                included in Javascript source code on a page. The client
                secret must be kept confidential.

        Returns:
            AccessTokenResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SHELL)
            .path('/token')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('grant_type')
                        .value(grant_type))
            .form_param(Parameter()
                        .key('client_id')
                        .value(client_id))
            .form_param(Parameter()
                        .key('client_secret')
                        .value(client_secret))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AccessTokenResponse.from_dictionary)
            .local_error('401', 'Unauthorized', AccessTokenErrorException)
        ).execute()

    def finalise_fueling(self,
                         body=None):
        """Does a POST request to /finaliseFueling.

        Enables Shell to inform partner of the successful completion of a
        transaction. Note this needs to be implemented over HTTPS

        Args:
            body (FinaliseFuelingRequest, optional): TODO: type description
                here.

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SHELL)
            .path('/finaliseFueling')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .body_serializer(APIHelper.json_serialize)
        ).execute()

    def cancel_fueling(self,
                       body=None):
        """Does a POST request to /cancelFueling.

        Enables Shell to inform partner that a Mobile Payment transaction has
        been cancelled by Shell as an error/issue occured. Note this needs to
        be implemented over HTTPS

        Args:
            body (CancelFuelingRequest, optional): TODO: type description here.

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SHELL)
            .path('/cancelFueling')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .body_serializer(APIHelper.json_serialize)
        ).execute()