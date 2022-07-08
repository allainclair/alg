from collections import defaultdict
from collections import Counter


def countMissingBadges(pairs):
    name_entries = defaultdict(list)
    for name, entry in pairs:
        name_entries[name].append(entry)

    sum_entered = sum_exited = 0
    for name, entries in name_entries.items():
        counter = Counter(entries)
        diff = counter['enter'] - counter['exit']
        if diff > 0:
            sum_exited += diff
        elif diff < 0:
            sum_entered += abs(diff)

    print(name_entries)
    print(f'Exited without badge: {sum_exited}')
    print(f'Entered without badge: {sum_entered}')


def main():
    entries = ['Kate', 'exit'], ['Silvia', 'exit'], ['Kate', 'exit']
    print(countMissingBadges(entries))


if __name__ == '__main__':
    main()