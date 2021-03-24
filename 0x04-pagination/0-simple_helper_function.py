#!/usr/bin/env python3
"""Index Range"""


def index_range(page: int, page_size: int) -> tuple:
    """
    -------------------
    METHOD: index_range
    -------------------
    Description:
        Takes in a starting page defined by page
        that acts as an offset and page_size
        that acts as the LIMIT.
    Args:
        @page      :offset
        @page_size :limit
    """
    if page <= 0:
        page = 1
    start = (page - 1) * page_size
    limit = page * page_size

    return (start, limit)
