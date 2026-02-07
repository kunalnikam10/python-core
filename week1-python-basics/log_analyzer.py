import json

log_file = "app.log"
summary_file = "summary.json"

log_counts = {
    "total_lines": 0,
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

try:
    with open(log_file, "r") as file:
        for line in file:
            log_counts["total_lines"] += 1
            
            if "INFO" in line:
                log_counts["INFO"] += 1
            elif "WARNING" in line:
                log_counts["WARNING"] += 1
            elif "ERROR" in line:
                log_counts["ERROR"] += 1

except FileNotFoundError:
    print("Log file not found.")
    exit()

except Exception as e:
    print("Unexpected error:", e)
    exit()

# Write summary to JSON
with open(summary_file, "w") as file:
    json.dump(log_counts, file, indent=4)

print("Log analysis completed. Summary saved to summary.json")