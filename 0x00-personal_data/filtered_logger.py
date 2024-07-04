#!/usr/bin/env python3
"""
    Module implementing logging with obfuscation

"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Uses regex to obfuscate and log data"""
    pattern = f"({'|'.join(fields)})=[^separator]*"
    # replacement = lambda m: f"{m.group(1)}={redaction}"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
