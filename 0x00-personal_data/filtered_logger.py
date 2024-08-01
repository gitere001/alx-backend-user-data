#!/usr/bin/env python3
"""a fuction to filter personal data"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Filters personal data from a message.

    Args:
        fields (List[str]): A list of fields to filter.
        redaction (str): The redaction to replace filtered fields with.
        message (str): The message to filter.
        separator (str): The separator between fields in the message.

    Returns:
        str: The filtered message.
    """
    for field in fields:
        message = re.sub(
            pattern=field + '=.*?' + separator,
            repl=field + '=' + redaction + separator,
            string=message,
        )
    return message
