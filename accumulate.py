import json, sys

REPORT_ITEMS = 'domain', 'button', 'cookie'
NEGATION = 'not '
NO_COOKIE = '(none)'


def accumulate_file(table, file):
    """Table is structured table[domain][button][cookie]"""
    failures = 0
    try:
        filedata = open(file)
    except:
        print('File does not exist:', file, sys.stderr)
        return

    for line in filedata:
        if not line.strip():
            continue
        try:
            report = json.loads(line)
        except:
            if not failures:
                print('File', file, 'does not contain a JSON list', sys.stderr)
            failures += 1
            continue

        domain, button, cookie = (report.get(i, '') for i in REPORT_ITEMS)
        cookie = cookie or NO_COOKIE
        if button.startswith(NEGATION):
            add = -1
            button = button[len(NEGATION):]
        else:
            add = 1

        btable = table.setdefault(domain, {}).setdefault(button, {})
        btable[cookie] = btable.get(cookie, 0) + add


def read_accumulate_write(table_file, *files):
    try:
        table_text = open(table_file)
    except:
        print('Starting new accumulator file', table_file)
        table = {}
    else:
        table = json.load(table_text)

    for file in files:
        accumulate_file(table, file)

    json.dump(table, open(table_file, 'w'))


if __name__ == '__main__':
    read_accumulate_write(*sys.argv[1:])
