from parser import parse_line
from stats import compute_stats
from filters import *
from exporter import export_json, export_csv

VALID = []
INVALID = {}

def load_file(path):
    global VALID, INVALID
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            parsed, errors = parse_line(line)

            if errors:
                INVALID[i] = errors
            else:
                VALID.append(parsed)


def main():
    load_file("test_logs.txt")

    print("\n=== VALID LOGS ===")
    for log in VALID:
        print(log)

    print("\n=== INVALID LOGS ===")
    for line_num, errs in INVALID.items():
        print(f"Line {line_num} errors: {errs}")

    stats = compute_stats(VALID)
    print("\n=== STATS ===")
    for k, v in stats.items():
        print(f"{k}: {v}")

    print("VALID:", len(VALID))
    print("INVALID:", len(INVALID))
    print(stats)

    export_json(VALID)
    export_csv(VALID)


if __name__ == "__main__":
    main()
