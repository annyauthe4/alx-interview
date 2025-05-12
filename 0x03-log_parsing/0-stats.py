#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:
- Total file size
- Count of valid status codes
Prints stats every 10 lines and on keyboard interruption (CTRL + C).
"""

import sys
import re
from collections import defaultdict

valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
status_counts = defaultdict(int)
total_file_size = 0
line_count = 0

# Pattern to match valid log line
pattern = re.compile(
    r'^\d{1,3}(?:\.\d{1,3}){3} - \[.*\] '
    r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
)


def print_stats():
    """Prints the current metrics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(valid_codes):
        count = status_counts.get(code, 0)
        if count:
            print("{}: {}".format(code, count))


try:
    for line in sys.stdin:
        line = line.strip()
        match = pattern.match(line)
        if match:
            status, size = match.groups()
            if status in valid_codes:
                status_counts[status] += 1
            try:
                total_file_size += int(size)
            except ValueError:
                pass
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
finally:
    print_stats()
