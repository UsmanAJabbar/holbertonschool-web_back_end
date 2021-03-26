#!/usr/bin/env python3
from typing import List
from re import sub as regex


def filter_datum(field: List[str], redaction: str, message: str, seperator: str) -> str:
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
