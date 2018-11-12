import json, sys


def apply_blacklist_rules(table, rules):
    blacklists = {}

    # `table` is structured table[domain][button][cookie]
    #
    # `rules` maps button names ('spam' or 'wrong') to a list of rules
    # Each rule is a dictionary mapping a cookie to a minimum value.
    #
    # `blacklists` maps button names to a set of domains

    for domain, dtable in table.items():
        for button, btable in dtable.items():
            for rule in rules.get(button, ()):
                if all(v <= btable.get(k, 0) for k, v in rule.items()):
                    blacklists.setdefault(button, set()).add(domain)

    return {k: sorted(v) for k, v in blacklists.items()}


def compute_blacklists(table_file, rules_file):
    table = json.load(open(table_file))
    rules = json.load(open(rules_file))
    return apply_blacklist_rules(table, rules)


def write_blacklist(table_file, rules_file, blacklist_file):
    blacklists = compute_blacklists(table_file, rules_file)
    json.dump(blacklists, open(blacklist_file, 'w'))


if __name__ == '__main__':
    write_blacklist(*sys.argv[1:])
