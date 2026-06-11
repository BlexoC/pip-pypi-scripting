from datetime import datetime


def generate_log(data):
    """Generate a log file from a list of entries."""

    # Validate input — must be a list
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")

    # Build filename with today's date e.g. log_20240611.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write each entry on its own line
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    return filename