import csv
from werkzeug.security import safe_join
import os

from src.commons.constants import FEEDBACK_CSV_HEADERS
from src.feedback.models import IssueType

def validate_csv_header(csvfile):
    csv_header = csvfile.stream.readline().decode().split(',')
    return csv_header == ['what bothers you?', 'age\n']


def feedback_issue_processor(upload_dir, filename):
    family_concern_freq = health_concern_freq = unknown_concern_freq = total_issues = 0
    with open(
        safe_join(os.fspath(upload_dir), os.fspath(filename)), 
        'r'
    ) as csvfile:
        for row in csv.DictReader(csvfile, FEEDBACK_CSV_HEADERS):
            concern = row['concern'].strip().casefold()
            age = row['age'].strip()
            if row['concern'] and age.isnumeric():
                row['age'] = int(age)
            else:
                raise ValueError(row)
            
            if 'family'.casefold() in concern and row['age'] > 25:
                family_concern_freq += 1
                row['classification'] = IssueType.FAMILY.value
            elif 'health'.casefold() in concern and row['age'] > 18:
                health_concern_freq += 1
                row['classification'] = IssueType.HEALTH.value
            else:
                unknown_concern_freq += 1
                row['classification'] = IssueType.UNKNOWN.value
            total_issues += 1
            yield row
    calc_pct_ratio = lambda freq:  (freq/total_issues) * 100
    
    if total_issues:
        yield {
            "family_concern_freq_ratio": calc_pct_ratio(family_concern_freq),
            "health_concern_freq_ratio": calc_pct_ratio(health_concern_freq),
            "unknown_concern_freq_ratio": calc_pct_ratio(unknown_concern_freq)
        }
    
