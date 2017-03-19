import csv

with open('submission-improv.csv', 'w') as submission_improv:
    w = csv.writer(submission_improv, quoting=csv.QUOTE_NONE)
    w.writerow(['id', 'label'])
    with open('submission.csv') as submission_file:
        r = csv.DictReader(submission_file)
        for row in r:
            p = float(row['label'])
            if p < 0.1:
                p = 0
            elif p > 0.9:
                p = 1
            w.writerow([row['id'], p])
