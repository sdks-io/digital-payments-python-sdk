# -*- coding: utf-8 -*-

"""
shellsmartpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellsmartpayapi.api_helper import APIHelper
from shellsmartpayapi.models.payment import Payment
from shellsmartpayapi.models.product import Product


class FinaliseFuelingRequest(object):

    """Implementation of the 'finaliseFuelingRequest' model.

    TODO: type model description here.

    Attributes:
        site_name (str): TODO: type description here.
        timestamp (long|int): TODO: type description here.
        volume_quantity (float): TODO: type description here.
        volume_unit (str): TODO: type description here.
        final_price (float): TODO: type description here.
        currency (str): TODO: type description here.
        status (str): TODO: type description here.
        site_address (str): TODO: type description here.
        original_price (float): TODO: type description here.
        discount (float): TODO: type description here.
        payment (Payment): TODO: type description here.
        products (List[Product]): TODO: type description here.
        mpp_transaction_id (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "site_name": 'siteName',
        "timestamp": 'timestamp',
        "volume_quantity": 'volumeQuantity',
        "volume_unit": 'volumeUnit',
        "final_price": 'finalPrice',
        "currency": 'currency',
        "status": 'status',
        "site_address": 'siteAddress',
        "original_price": 'originalPrice',
        "discount": 'discount',
        "payment": 'payment',
        "products": 'products',
        "mpp_transaction_id": 'mppTransactionId'
    }

    _optionals = [
        'site_name',
        'timestamp',
        'volume_quantity',
        'volume_unit',
        'final_price',
        'currency',
        'status',
        'site_address',
        'original_price',
        'discount',
        'payment',
        'products',
        'mpp_transaction_id',
    ]

    def __init__(self,
                 site_name=APIHelper.SKIP,
                 timestamp=APIHelper.SKIP,
                 volume_quantity=APIHelper.SKIP,
                 volume_unit=APIHelper.SKIP,
                 final_price=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 site_address=APIHelper.SKIP,
                 original_price=APIHelper.SKIP,
                 discount=APIHelper.SKIP,
                 payment=APIHelper.SKIP,
                 products=APIHelper.SKIP,
                 mpp_transaction_id=APIHelper.SKIP):
        """Constructor for the FinaliseFuelingRequest class"""

        # Initialize members of the class
        if site_name is not APIHelper.SKIP:
            self.site_name = site_name 
        if timestamp is not APIHelper.SKIP:
            self.timestamp = timestamp 
        if volume_quantity is not APIHelper.SKIP:
            self.volume_quantity = volume_quantity 
        if volume_unit is not APIHelper.SKIP:
            self.volume_unit = volume_unit 
        if final_price is not APIHelper.SKIP:
            self.final_price = final_price 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if status is not APIHelper.SKIP:
            self.status = status 
        if site_address is not APIHelper.SKIP:
            self.site_address = site_address 
        if original_price is not APIHelper.SKIP:
            self.original_price = original_price 
        if discount is not APIHelper.SKIP:
            self.discount = discount 
        if payment is not APIHelper.SKIP:
            self.payment = payment 
        if products is not APIHelper.SKIP:
            self.products = products 
        if mpp_transaction_id is not APIHelper.SKIP:
            self.mpp_transaction_id = mpp_transaction_id 

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
        site_name = dictionary.get("siteName") if dictionary.get("siteName") else APIHelper.SKIP
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else APIHelper.SKIP
        volume_quantity = dictionary.get("volumeQuantity") if dictionary.get("volumeQuantity") else APIHelper.SKIP
        volume_unit = dictionary.get("volumeUnit") if dictionary.get("volumeUnit") else APIHelper.SKIP
        final_price = dictionary.get("finalPrice") if dictionary.get("finalPrice") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        site_address = dictionary.get("siteAddress") if dictionary.get("siteAddress") else APIHelper.SKIP
        original_price = dictionary.get("originalPrice") if dictionary.get("originalPrice") else APIHelper.SKIP
        discount = dictionary.get("discount") if dictionary.get("discount") else APIHelper.SKIP
        payment = Payment.from_dictionary(dictionary.get('payment')) if 'payment' in dictionary.keys() else APIHelper.SKIP
        products = None
        if dictionary.get('products') is not None:
            products = [Product.from_dictionary(x) for x in dictionary.get('products')]
        else:
            products = APIHelper.SKIP
        mpp_transaction_id = dictionary.get("mppTransactionId") if dictionary.get("mppTransactionId") else APIHelper.SKIP
        # Return an object of this model
        return cls(site_name,
                   timestamp,
                   volume_quantity,
                   volume_unit,
                   final_price,
                   currency,
                   status,
                   site_address,
                   original_price,
                   discount,
                   payment,
                   products,
                   mpp_transaction_id)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'site_name={self.site_name!r}, '
                f'timestamp={self.timestamp!r}, '
                f'volume_quantity={self.volume_quantity!r}, '
                f'volume_unit={self.volume_unit!r}, '
                f'final_price={self.final_price!r}, '
                f'currency={self.currency!r}, '
                f'status={self.status!r}, '
                f'site_address={self.site_address!r}, '
                f'original_price={self.original_price!r}, '
                f'discount={self.discount!r}, '
                f'payment={self.payment!r}, '
                f'products={self.products!r}, '
                f'mpp_transaction_id={self.mpp_transaction_id!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'site_name={self.site_name!s}, '
                f'timestamp={self.timestamp!s}, '
                f'volume_quantity={self.volume_quantity!s}, '
                f'volume_unit={self.volume_unit!s}, '
                f'final_price={self.final_price!s}, '
                f'currency={self.currency!s}, '
                f'status={self.status!s}, '
                f'site_address={self.site_address!s}, '
                f'original_price={self.original_price!s}, '
                f'discount={self.discount!s}, '
                f'payment={self.payment!s}, '
                f'products={self.products!s}, '
                f'mpp_transaction_id={self.mpp_transaction_id!s})')
