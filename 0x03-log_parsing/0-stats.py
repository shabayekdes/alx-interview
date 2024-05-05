#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics
"""

import sys
import re
from collections import defaultdict

LOG_REGEX = re.compile(
    r'^(\d+\.\d+\.\d+\.\d+) - \[.*\] '
    r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
)


def process_logs():
    file_size_total = 0
    status_code_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            match = LOG_REGEX.match(line)
            if not match:
                continue

            ip_address, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)

            file_size_total += file_size

            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_code_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                line_count = 0
                print_stats(file_size_total, status_code_counts)

    except KeyboardInterrupt:
        print_stats(file_size_total, status_code_counts)

    finally:
        print_stats(file_size_total, status_code_counts)


def print_stats(file_size_total, status_code_counts):
    print(f"File size: {file_size_total}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")
    print()


if __name__ == "__main__":
    process_logs()
