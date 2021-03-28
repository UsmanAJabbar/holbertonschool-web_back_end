#!/usr/bin/env python3
from typing import List
from re import sub as regex
import logging
from mysql.connector import connect as conn
PII_FIELDS = ('name', 'email', 'ssn', 'phone', 'password')

def filter_datum(field: List[str],
                 redaction: str,
                 message: str,
                 seperator: str) -> str:
    """
    --------------------
    METHOD: filter_datum
    --------------------
    Description:
        Takes in a number of parameters with
        seperators and returns the data that
        needs to be obfuscated as a string
    Args:
        @fields    : list of strings with fields to obfuscate.
        @redaction : string representing what to obfuscate with.
        @message   : string representing the log line.
        @separator : seperator seperating individual fields.
    """
    for fieldname in field:
        message = regex(f'{fieldname}=.+?{seperator}',
                        f"{fieldname}={redaction}{seperator}",
                        message)
    return message

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        """Initialize"""
        self.fields = list(fields)
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Format method that redacts sensitive information"""
        return filter_datum(self.fields,
                            self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)

def get_logger() -> logging.Logger:
    """
    ------------------
    METHOD: get_logger
    ------------------
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler(RedactingFormatter(fields=PII_FIELDS))

    logger.addHandler(handler)

    return logger


def get_db() -> conn:
    """
    --------------
    METHOD: get_db
    --------------
    Description:
        Takes no arguments, but returns
        a connection to the database.
    """
    from os import environ as env

    b = 'PERSONAL_DATA_DB_'
    usr, pwd, host, db = env[b+'USERNAME'], env[b+'PASSWORD'], env[b+'HOST'], env[b+'NAME']

    return conn(user=usr, password=pwd, host=host, database=db)