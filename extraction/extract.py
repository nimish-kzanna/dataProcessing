import csv
import json
import sys
import os

def main():
    """
    Script to extract the message_text from the raw data
    """

    input_file_path = "data.txt"
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
    output_file_path = "extracted.csv"
    custom_output_file_path = "../customParser/data"  # Updated path

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(custom_output_file_path), exist_ok=True)

    with open(input_file_path, "r") as input_file, open(output_file_path, "w", newline="") as output_file, open(os.path.join(custom_output_file_path, "log"), "w", newline="") as custom_output_file:
        writer = csv.writer(output_file)
        custom_writer = csv.writer(custom_output_file)
        writer.writerow(["message_text"])

        for line in input_file:
            try:
                data = json.loads(line)
                message_text = data.get("message_text")
                if isinstance(message_text, str):
                    writer.writerow([message_text])
                    custom_writer.writerow([message_text])
                else:
                    print(f"Key 'message_text' not found or not a string in line: {line.strip()}")
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")

    print(f"Extraction complete. Values written to {output_file_path} and {os.path.join(custom_output_file_path, 'log')}")

if __name__ == "__main__":
    main()