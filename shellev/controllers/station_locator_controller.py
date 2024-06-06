# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from shellev.api_helper import APIHelper
from shellev.configuration import Server
from shellev.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from shellev.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from shellev.models.around_location_array import AroundLocationArray
from shellev.exceptions.station_locator_bad_request_exception import StationLocatorBadRequestException
from shellev.exceptions.station_locator_unauthorized_exception import StationLocatorUnauthorizedException
from shellev.exceptions.station_locator_forbidden_exception import StationLocatorForbiddenException
from shellev.exceptions.station_locator_not_found_exception import StationLocatorNotFoundException
from shellev.exceptions.station_locator_internal_server_error_exception import StationLocatorInternalServerErrorException


class StationLocatorController(BaseController):

    """A Controller to access Endpoints in the shellev API."""
    def __init__(self, config):
        super(StationLocatorController, self).__init__(config)

    def stationlocator_v_1_stations_get_around_location(self,
                                                        m,
                                                        lon,
                                                        lat,
                                                        radius,
                                                        offer_code=None,
                                                        n=None,
                                                        amenities=None,
                                                        countries=None):
        """Does a GET request to /SiteData/v1/stations/.

        Returns all sites within specified radius of specified GPS location.
        Sites of all Types are returned. This call must be used when
        attempting to establish the station the user is located at as part of
        fuelling journey (i.e. user has to be within 300m of station to be
        considered located at the station). This API could also be used as a
        general query to find nearby Shell locations

        Args:
            m (str): API Method to be executed
            lon (float): The user’s current longitude
            lat (float): The user’s current latitude
            radius (float): The search radius in kilometers
            offer_code (str, optional): This enables requestor to specify
                locations that will honour the specified (advanced) offer
                code
            n (int, optional): This enables requestor to limit the number of
                locations that are returned and defaulted to a maximum of 250
                locations. Locations returned based on distance to User’s
                location as-the-crow-flies.
            amenities (List[str], optional): This enables requestor to filter
                locations based on one or more amenities (e.g. Filter
                locations so that only those with a Toilet are returned).
            countries (List[str], optional): This enables requestor to filter
                locations based on one or more Countries (i.e. by country
                codes).

        Returns:
            AroundLocationArray: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/SiteData/v1/stations/')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('m')
                         .value(m))
            .query_param(Parameter()
                         .key('lon')
                         .value(lon))
            .query_param(Parameter()
                         .key('lat')
                         .value(lat))
            .query_param(Parameter()
                         .key('radius')
                         .value(radius))
            .query_param(Parameter()
                         .key('offer_code')
                         .value(offer_code))
            .query_param(Parameter()
                         .key('n')
                         .value(n))
            .query_param(Parameter()
                         .key('amenities')
                         .value(amenities))
            .query_param(Parameter()
                         .key('countries')
                         .value(countries))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuthTokenPost'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AroundLocationArray.from_dictionary)
            .local_error('400', 'Bad request', StationLocatorBadRequestException)
            .local_error('401', 'Unauthorized', StationLocatorUnauthorizedException)
            .local_error('403', 'Forbbiden', StationLocatorForbiddenException)
            .local_error('404', 'Not Found', StationLocatorNotFoundException)
            .local_error('500', 'Internal Server Error', StationLocatorInternalServerErrorException)
        ).execute()
