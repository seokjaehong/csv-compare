import os
from datetime import datetime


def _diff_and_summarize(from_csv, to_csv, index_columns,
                        sep=',', ignored_columns=None, significance=None):
    """
    Print a summary of the difference between the two files.
    """
    from csvdiff import records
    from_records = list(records.load(from_csv, sep=sep))
    user_size = len(list(records.load(to_csv, sep=sep)))

    to_records = records.load(to_csv, sep=sep)

    from csvdiff import patch
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


if __name__ == '__main__':

    file_a = "./testcase6.csv"
    user_file = "./test.csv"
    file_size = os.path.getsize(file_a)
    print('file_size(MB)', round(file_size / (1024 * 1024), 2))

    start_time = datetime.now()
    # print('시작시간',start_time )

    boolean, detail = _diff_and_summarize(file_a, user_file, ['PassengerId'], sep=',')
    n_removed, n_added, n_changed, orig_size, user_size = detail[0], detail[1], detail[2], detail[3], detail[4]
    if boolean:

        diff_count = n_removed + n_added + n_changed
        score = 100 - 100 * (diff_count / orig_size)
        if n_removed or n_added or n_changed:
            # print('{0}의 채점결과입니다.'.format(user_file))

            # print('----------------ROW 기준 내용------------------')
            print('비교 ROW의 개수는 {0}개 입니다.'.format(orig_size))
            # print(u'%d rows 가 제거되었습니다. (%.01f%%)' % (n_removed, 100 * n_removed / orig_size))
            # print(u'%d rows 가 추가되었습니다. (%.01f%%)' % (n_added, 100 * n_added / orig_size))
            # print(u'%d rows 가 변경되었습니다. (%.01f%%)' % (n_changed, 100 * n_changed / orig_size))
            # print('{0}개의 차이가 발생합니다.\n'.format(diff_count))
            # print('----------------DATA 기준 내용------------------')
        print('{0}점입니다'.format(round(score, 2)))
        end_time = datetime.now()
        # print('종료시간',end_time )
        duration = end_time - start_time

        print('채점 소요시간(s): ', duration.total_seconds())

        # record = csvdiff.diff_fies(file_a, user_file, ['PassengerId'], sep=',')
        # print(record)

        # changed_data = record['changed']
        # diff_col_cnt = len([x['key'] for x in changed_data])
        # diff_data_cnt = sum([len(value['fields']) for value in changed_data])
        # print('{0}개의 데이터에서 다른점이 발견되었습니다'.format(diff_data_cnt))

    else:
        print(detail)
