import json
import csv


def export_json(logs, filename="valid_logs.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(logs, f, default=str, indent=4)


def export_csv(logs, filename="valid_logs.csv"):
    if not logs:
        print("No valid logs to export.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=logs[0].keys())
        writer.writeheader()
        writer.writerows(logs)
    print('CSV export complete.')
