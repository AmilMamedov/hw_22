# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    read_data = _read(csv)
    sort_data = _sort(read_data)
    filter_data = _filter(sort_data)
    return filter_data


def _read(csv):
    return [item.split(';') for item in csv.split('\n')]


def _sort(data, reverse=True):
    return sorted(data, reverse=reverse)


def _filter(data):
    return [item for item in data if int(item[1]) > 10]


if __name__ == '__main__':
    print(get_users_list())
