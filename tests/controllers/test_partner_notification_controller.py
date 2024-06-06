# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from shellev.api_helper import APIHelper
from shellev.models.finalise_fueling_request import FinaliseFuelingRequest
from shellev.models.cancel_fueling_request import CancelFuelingRequest


class PartnerNotificationControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(PartnerNotificationControllerTests, cls).setUpClass()
        cls.controller = cls.client.partner_notification
        cls.response_catcher = cls.controller.http_call_back

    # To access the Partner’s endpoints, for sending callback messages, Shell will need to connect to the Partner API end points. It is recemmended that the partner offers OAuth 2.0 as a standard for call back APIs and will require the OAuth 2.0 token for authentication. Note this needs to be implemented over HTTPS
    def test_partner_token(self):
        # Parameters for the API call
        grant_type = 'client_credentials'
        client_id = 'SOFflRakNlwnWlxfOXQ4GHDVyqGawuKA'
        client_secret = 'cRnWgw7gACqM3gVS'

        # Perform the API call through the SDK function
        result = self.controller.partner_token(grant_type, client_id, client_secret)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Enables Shell to inform partner of the successful completion of a transaction. Note this needs to be implemented over HTTPS
    def test_finalise_fueling(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        self.controller.finalise_fueling(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

    # Enables Shell to inform partner that a Mobile Payment transaction has been cancelled by Shell as an error/issue occured. Note this needs to be implemented over HTTPS
    def test_cancel_fueling(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        self.controller.cancel_fueling(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

