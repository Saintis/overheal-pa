"""
Readers module, collection of code to handle reading in the data for analysis.

By: Filip Gokstorp (Saintis), 2020
"""
from .reader import APIProcessor, get_heals

def url_to_code(source):
    """Converts a url to a source"""
    return source.split("#")[0].split("/")[-1]


def read_heals(source, **kwargs):
    """
    Read data from specified source
    """

    if "https://" in source or "http://" in source:
        code = url_to_code(source)
    else:
        # Try assuming source is just the code
        code = source

    try:
        heals = get_heals(code, **kwargs)
    except IOError as e:
        return None, e

    return heals, None


def get_processor(source, **kwargs):
    """
    Get a data processor for the specified source
    """
    # Assuming source is a url pointing towards a WCL report, or the report code itself
    if "https://" in source or "http://" in source:
        source = url_to_code(source)

    return APIProcessor(source, **kwargs)
