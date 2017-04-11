from solution import binary_search

scenarios = [
    [2, 3, 4, 5, 9],
    [0, 9, 41, 53, 76, 79, 81, 84, 89, 95]
]


for scenario in scenarios:
    print('begin scenario={}'.format(scenario))
    print('target={} index={}'.format(5, binary_search(scenario, 5)))
    print('target={} index={}'.format(9, binary_search(scenario, 9)))
    print('target={} index={}'.format(79, binary_search(scenario, 79)))
    print('target={} index={}'.format(13, binary_search(scenario, 13)))
