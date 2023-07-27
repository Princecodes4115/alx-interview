#!/usr/bin/python3
import sys
import signal

status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
total_size = 0
status_counts = {code: 0 for code in status_codes}

def print_statistics():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

line_count = 0
for line in sys.stdin:
    try:
        parts = line.split()
        ip_address, _, _, status_code, file_size = parts[0], parts[5], parts[8], int(parts[-2]), int(parts[-1])
        if status_code in status_codes:
            total_size += file_size
            status_counts[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_statistics()
    except (ValueError, IndexError):
        continue

print_statistics()

