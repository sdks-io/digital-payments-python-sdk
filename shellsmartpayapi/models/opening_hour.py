# -*- coding: utf-8 -*-

"""
shellsmartpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellsmartpayapi.api_helper import APIHelper


class OpeningHour(object):

    """Implementation of the 'OpeningHour' model.

    Attributes:
        closing_from_hours (str): The model property of type str.
        closing_from_minutes (str): The model property of type str.
        closing_to_hours (str): The model property of type str.
        closing_to_minutes (str): The model property of type str.
        from_day (str): The model property of type str.
        opening_from_hours (str): The model property of type str.
        opening_from_minutes (str): The model property of type str.
        opening_to_hours (str): The model property of type str.
        opening_to_minutes (str): The model property of type str.
        to_day (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "closing_from_hours": 'Closing_From_Hours',
        "closing_from_minutes": 'Closing_From_Minutes',
        "closing_to_hours": 'Closing_To_Hours',
        "closing_to_minutes": 'Closing_To_Minutes',
        "from_day": 'From_Day',
        "opening_from_hours": 'Opening_From_Hours',
        "opening_from_minutes": 'Opening_From_Minutes',
        "opening_to_hours": 'Opening_To_Hours',
        "opening_to_minutes": 'Opening_To_Minutes',
        "to_day": 'To_Day'
    }

    _optionals = [
        'closing_from_hours',
        'closing_from_minutes',
        'closing_to_hours',
        'closing_to_minutes',
        'from_day',
        'opening_from_hours',
        'opening_from_minutes',
        'opening_to_hours',
        'opening_to_minutes',
        'to_day',
    ]

    def __init__(self,
                 closing_from_hours=APIHelper.SKIP,
                 closing_from_minutes=APIHelper.SKIP,
                 closing_to_hours=APIHelper.SKIP,
                 closing_to_minutes=APIHelper.SKIP,
                 from_day=APIHelper.SKIP,
                 opening_from_hours=APIHelper.SKIP,
                 opening_from_minutes=APIHelper.SKIP,
                 opening_to_hours=APIHelper.SKIP,
                 opening_to_minutes=APIHelper.SKIP,
                 to_day=APIHelper.SKIP):
        """Constructor for the OpeningHour class"""

        # Initialize members of the class
        if closing_from_hours is not APIHelper.SKIP:
            self.closing_from_hours = closing_from_hours 
        if closing_from_minutes is not APIHelper.SKIP:
            self.closing_from_minutes = closing_from_minutes 
        if closing_to_hours is not APIHelper.SKIP:
            self.closing_to_hours = closing_to_hours 
        if closing_to_minutes is not APIHelper.SKIP:
            self.closing_to_minutes = closing_to_minutes 
        if from_day is not APIHelper.SKIP:
            self.from_day = from_day 
        if opening_from_hours is not APIHelper.SKIP:
            self.opening_from_hours = opening_from_hours 
        if opening_from_minutes is not APIHelper.SKIP:
            self.opening_from_minutes = opening_from_minutes 
        if opening_to_hours is not APIHelper.SKIP:
            self.opening_to_hours = opening_to_hours 
        if opening_to_minutes is not APIHelper.SKIP:
            self.opening_to_minutes = opening_to_minutes 
        if to_day is not APIHelper.SKIP:
            self.to_day = to_day 

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
        closing_from_hours = dictionary.get("Closing_From_Hours") if dictionary.get("Closing_From_Hours") else APIHelper.SKIP
        closing_from_minutes = dictionary.get("Closing_From_Minutes") if dictionary.get("Closing_From_Minutes") else APIHelper.SKIP
        closing_to_hours = dictionary.get("Closing_To_Hours") if dictionary.get("Closing_To_Hours") else APIHelper.SKIP
        closing_to_minutes = dictionary.get("Closing_To_Minutes") if dictionary.get("Closing_To_Minutes") else APIHelper.SKIP
        from_day = dictionary.get("From_Day") if dictionary.get("From_Day") else APIHelper.SKIP
        opening_from_hours = dictionary.get("Opening_From_Hours") if dictionary.get("Opening_From_Hours") else APIHelper.SKIP
        opening_from_minutes = dictionary.get("Opening_From_Minutes") if dictionary.get("Opening_From_Minutes") else APIHelper.SKIP
        opening_to_hours = dictionary.get("Opening_To_Hours") if dictionary.get("Opening_To_Hours") else APIHelper.SKIP
        opening_to_minutes = dictionary.get("Opening_To_Minutes") if dictionary.get("Opening_To_Minutes") else APIHelper.SKIP
        to_day = dictionary.get("To_Day") if dictionary.get("To_Day") else APIHelper.SKIP
        # Return an object of this model
        return cls(closing_from_hours,
                   closing_from_minutes,
                   closing_to_hours,
                   closing_to_minutes,
                   from_day,
                   opening_from_hours,
                   opening_from_minutes,
                   opening_to_hours,
                   opening_to_minutes,
                   to_day)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'closing_from_hours={(self.closing_from_hours if hasattr(self, "closing_from_hours") else None)!r}, '
                f'closing_from_minutes={(self.closing_from_minutes if hasattr(self, "closing_from_minutes") else None)!r}, '
                f'closing_to_hours={(self.closing_to_hours if hasattr(self, "closing_to_hours") else None)!r}, '
                f'closing_to_minutes={(self.closing_to_minutes if hasattr(self, "closing_to_minutes") else None)!r}, '
                f'from_day={(self.from_day if hasattr(self, "from_day") else None)!r}, '
                f'opening_from_hours={(self.opening_from_hours if hasattr(self, "opening_from_hours") else None)!r}, '
                f'opening_from_minutes={(self.opening_from_minutes if hasattr(self, "opening_from_minutes") else None)!r}, '
                f'opening_to_hours={(self.opening_to_hours if hasattr(self, "opening_to_hours") else None)!r}, '
                f'opening_to_minutes={(self.opening_to_minutes if hasattr(self, "opening_to_minutes") else None)!r}, '
                f'to_day={(self.to_day if hasattr(self, "to_day") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'closing_from_hours={(self.closing_from_hours if hasattr(self, "closing_from_hours") else None)!s}, '
                f'closing_from_minutes={(self.closing_from_minutes if hasattr(self, "closing_from_minutes") else None)!s}, '
                f'closing_to_hours={(self.closing_to_hours if hasattr(self, "closing_to_hours") else None)!s}, '
                f'closing_to_minutes={(self.closing_to_minutes if hasattr(self, "closing_to_minutes") else None)!s}, '
                f'from_day={(self.from_day if hasattr(self, "from_day") else None)!s}, '
                f'opening_from_hours={(self.opening_from_hours if hasattr(self, "opening_from_hours") else None)!s}, '
                f'opening_from_minutes={(self.opening_from_minutes if hasattr(self, "opening_from_minutes") else None)!s}, '
                f'opening_to_hours={(self.opening_to_hours if hasattr(self, "opening_to_hours") else None)!s}, '
                f'opening_to_minutes={(self.opening_to_minutes if hasattr(self, "opening_to_minutes") else None)!s}, '
                f'to_day={(self.to_day if hasattr(self, "to_day") else None)!s})')
