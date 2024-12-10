#!/usr/bin/env python3
"""
This module provides a method for calculating
the start and end indices
for paginated data.

Typical usage example:
index_range(page, page_size)
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing a start
    index and an end index.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the
        start index (inclusive) and 
        end index (exclusive) for the items on the given page.
    """
    pass
