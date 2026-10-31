# test.py (in project root)
import sys
from pathlib import Path
import csv
sys.path.insert(0, str(Path(__file__).resolve().parent / 'src'))
csv_path = Path(__file__).resolve().parent / 'data' / 'emails.csv'
from classifier import classify_email   





with open(csv_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        predicted_label = classify_email(row['subject'], row['body'])
        print("The avg accuracy of the model is: ", (predicted_label == row['label']) / len(list(reader)))
