import csv
from werkzeug.security import safe_join
import os

from src.commons.constants import FEEDBACK_CSV_HEADERS

def validate_csv_header(csvfile):
    csv_header = csvfile.stream.readline().decode().split(',')
    return csv_header == ['what bothers you?', 'age\n']


def normalize_csv(upload_dir, filename):
    with open(
        safe_join(os.fspath(upload_dir), os.fspath(filename)), 
        'r'
    ) as csvfile:
        for row in csv.DictReader(csvfile, FEEDBACK_CSV_HEADERS):
            if row['concern'] and row['age'].isnumeric():
                row['age'] = int(row['age'])
                yield row
            else:
                raise ValueError()
