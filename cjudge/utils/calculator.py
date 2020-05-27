import math
import os
from csvdiff import records, patch


def _diff_and_summarize(from_csv, to_csv, index_columns,
                        sep=',', ignored_columns=None, significance=None):
    from_records = list(records.load(from_csv, sep=sep))
    user_size = len(list(records.load(to_csv, sep=sep)))

    to_records = list(records.load(to_csv, sep=sep))

    try:
        diff = patch.create(from_records, to_records, index_columns, ignored_columns)
    except KeyError:
        error_message = "column does not matched"
        return False, error_message
    if significance is not None:
        diff = patch.filter_significance(diff, significance)

    orig_size = len(from_records)
    if orig_size == 0:
        orig_size = 1

    n_removed = len(diff['removed'])
    n_added = len(diff['added'])
    n_changed = len(diff['changed'])
    return True, (n_removed, n_added, n_changed, orig_size, user_size)


def calculate_csv(submission):
    user_file = submission.docfile.path
    file_a = "./testcase6.csv"
    result = {
        'file_size': "{:,}".format(os.path.getsize(file_a)),
        'score': 0,
        'n_removed': 0,
        'n_added': 0,
        'n_changed': 0,
        'duration': 0
    }

    from datetime import datetime
    start_time = datetime.now()

    boolean, detail = _diff_and_summarize(file_a, user_file, ['PassengerId'], sep=',')
    n_removed, n_added, n_changed, orig_size, user_size = detail[0], detail[1], detail[2], detail[3], detail[4]
    if boolean:
        diff_count = n_removed + n_added + n_changed
        print(diff_count,n_removed,orig_size)
        score = round(100 - 100 * (diff_count / orig_size),2)
        result['score'] = score
        if n_removed or n_added or n_changed:
            result['n_removed'] = n_removed
            result['n_added'] = n_added
            result['n_changed'] = n_changed
        end_time = datetime.now()
        result['duration'] = round((end_time - start_time).total_seconds(), 2)
        return True, result
    else:
        return False, detail
