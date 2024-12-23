# -*- coding: utf-8 -*-

"""
shellsmartpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from shellsmartpayapi.configuration import Configuration
from shellsmartpayapi.controllers.base_controller import BaseController
from shellsmartpayapi.configuration import Environment
from shellsmartpayapi.http.auth.mpp_token import MppToken
from shellsmartpayapi.http.auth.o_auth_token_post import OAuthTokenPost
from shellsmartpayapi.controllers.shell_api_platform_security_authentication_controller\
    import ShellAPIPlatformSecurityAuthenticationController
from shellsmartpayapi.controllers.digital_payment_enablement_controller\
    import DigitalPaymentEnablementController
from shellsmartpayapi.controllers.station_locator_controller\
    import StationLocatorController
from shellsmartpayapi.controllers.fueling_controller import FuelingController
from shellsmartpayapi.controllers.partner_notification_controller\
    import PartnerNotificationController


class ShellsmartpayapiClient(object):
    @LazyProperty
    def shell_api_platform_security_authentication(self):
        return ShellAPIPlatformSecurityAuthenticationController(self.global_configuration)

    @LazyProperty
    def digital_payment_enablement(self):
        return DigitalPaymentEnablementController(self.global_configuration)

    @LazyProperty
    def station_locator(self):
        return StationLocatorController(self.global_configuration)

    @LazyProperty
    def fueling(self):
        return FuelingController(self.global_configuration)

    @LazyProperty
    def partner_notification(self):
        return PartnerNotificationController(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment=Environment.TEST, mpp_token_credentials=None,
                 o_auth_token_post_credentials=None, config=None):
        self.config = config or Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            environment=environment,
            mpp_token_credentials=mpp_token_credentials,
            o_auth_token_post_credentials=o_auth_token_post_credentials)

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseController.user_agent(), BaseController.user_agent_parameters())

        self.auth_managers = {key: None for key in ['MppToken',
                                                    'oAuthTokenPost']}
        self.auth_managers['MppToken'] = MppToken(
            self.config.mpp_token_credentials)
        self.auth_managers['oAuthTokenPost'] = OAuthTokenPost(
            self.config.o_auth_token_post_credentials)
        self.global_configuration = self.global_configuration.auth_managers(self.auth_managers)

