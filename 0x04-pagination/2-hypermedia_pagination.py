#!/usr/bin/env python3
"""Server Object"""
from typing import List
import csv
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        init
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        ----------------
        METHOD: get_page
        ----------------
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        start = index_range(page, page_size)[0]
        end = index_range(page, page_size)[1]

        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        ----------------
        METHOD: get_page
        ----------------
        """
        dataset = self.get_page(page, page_size)

        page_count = len(self.dataset()) / page_size
        if int(page_count) < page_count:
            page_count = int(page_count) + 1

        schema = {
            'page_size': len(dataset),
            'page': page,
            'data': dataset,
            'next_page': page + 1 if page + 1 <= (len(self.dataset()) // page_size) else None,
            'prev_page': page - 1 if page - 1 > 0 else None,
            'total_pages': int(page_count)
        }

        return schema
