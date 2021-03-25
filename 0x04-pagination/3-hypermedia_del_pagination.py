#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""
from typing import List, Dict
import csv
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"
    data_rows = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def __init__(self):
        self.__dataset = None
        self.data_rows = self.dataset()
        self.__indexed_dataset = None
    
    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        -----------------------
        METHOD: get_hyper_index
        -----------------------
        """
        assert type(index) == int
        assert index <= index_range(index, page_size)[0]

        start, end = index, index + page_size
        schema = {
            'index': start,
            'data': self.data_rows[start:end],
            'next_index': None if end + 1 >= len(self.data_rows) else end,
            'page_size': page_size
        }
        return schema