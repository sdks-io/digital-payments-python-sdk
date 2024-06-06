# -*- coding: utf-8 -*-

"""
shellev

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellev.api_helper import APIHelper


class MppError(object):

    """Implementation of the 'MppError' model.

    TODO: type model description here.

    Attributes:
        message (str): Descriptive, human readable error message. Description
            of the error (e.g. This field is required and must to be between 1
            and 255 characters long)
        reason (str): Additional classification specific for each error type
            e.g. 'noStock'. The nature of the issue (e.g. missing)
        subject (str): Identifier of the related object e.g. '1'. The
            field/attribute with an issue (e.g. First Name)
        subject_type (str): Type of the object related to the error e.g.
            'entry'. The item it relates to (e.g. Parameter)
        mtype (str): Type of the error e.g. 'LowStockError', 'Validation
            Error'

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message": 'message',
        "reason": 'reason',
        "subject": 'subject',
        "subject_type": 'subjectType',
        "mtype": 'type'
    }

    _optionals = [
        'message',
        'reason',
        'subject',
        'subject_type',
        'mtype',
    ]

    def __init__(self,
                 message=APIHelper.SKIP,
                 reason=APIHelper.SKIP,
                 subject=APIHelper.SKIP,
                 subject_type=APIHelper.SKIP,
                 mtype=APIHelper.SKIP):
        """Constructor for the MppError class"""

        # Initialize members of the class
        if message is not APIHelper.SKIP:
            self.message = message 
        if reason is not APIHelper.SKIP:
            self.reason = reason 
        if subject is not APIHelper.SKIP:
            self.subject = subject 
        if subject_type is not APIHelper.SKIP:
            self.subject_type = subject_type 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 

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
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        reason = dictionary.get("reason") if dictionary.get("reason") else APIHelper.SKIP
        subject = dictionary.get("subject") if dictionary.get("subject") else APIHelper.SKIP
        subject_type = dictionary.get("subjectType") if dictionary.get("subjectType") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        # Return an object of this model
        return cls(message,
                   reason,
                   subject,
                   subject_type,
                   mtype)
