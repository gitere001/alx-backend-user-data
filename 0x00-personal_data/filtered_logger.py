#!/usr/bin/env python3
"""a fuction to filter personal data"""

import re
from typing import List
import logging

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        redact the message of LogRecord instance
        Args:
        record (logging.LogRecord): LogRecord instance containing message
        Return:
            formatted string
        """
        message = super(RedactingFormatter, self).format(record)
        redacted = filter_datum(self.fields, self.REDACTION,
                                message, self.SEPARATOR)
        return redacted


def get_logger() -> logging.Logger:
    """
    Return a logging.Logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()

    formatter = RedactingFormatter(PII_FIELDS)

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
