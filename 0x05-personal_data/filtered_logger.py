#!/usr/bin/env python3
"""Doc"""
from typing import List
from re import sub as regex
import logging
import mysql.connector
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

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))

    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    --------------
    METHOD: get_db
    --------------
    Description:
        Takes no arguments, but returns
        a connection to the database.
    """
    from os import environ as env

    usr = env['PERSONAL_DATA_DB_USERNAME']
    pwd = env['PERSONAL_DATA_DB_PASSWORD']
    host = env['PERSONAL_DATA_DB_HOST']
    db = env['PERSONAL_DATA_DB_NAME']

    return mysql.connector.connect(user=usr,
                                   password=pwd,
                                   host=host,
                                   database=db)


if __name__ == "main":
    """Main"""
    db_data = get_db()
    db_query = db_data.cursor()
    db_query.execute('SELECT * FROM users;')

    for rows in db_query:
        print(''.join(str(rows)))
