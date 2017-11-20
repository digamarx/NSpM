import generator
import generator_utils
import operator


def test_extract_variables():
    query = 'select distinct(?x) ?y where { ?x a C . ?x a ?y }'
    query2 = 'select distinct ?a where'

    result = generator_utils.extract_variables(query)
    result2 = generator_utils.extract_variables(query2)

    assert result == ['x', 'y']
    assert result2 == ['a']


def test_single_resource_sort():
    matches = [{'usages': [17]}, {'usages': [0]}, {'usages': [3]}, {'usages': [2]}, {'usages': [1]}]

    result = sorted(matches, key=generator.prioritize_usage)

    assert map(operator.itemgetter(0), map(operator.itemgetter('usages'), result)) == [17, 3, 2, 1, 0 ]


def test_couple_resource_sort():
    matches = [{'usages': [17, 2]}, {'usages': [0, 0]}, {'usages': [3, 2]}, {'usages': [2, 2]}, {'usages': [1, 2]}]

    result = sorted(matches, key=generator.prioritize_usage)

    assert map(operator.itemgetter('usages'), result) == [ [17, 2], [3, 2], [2, 2], [1, 2], [0, 0]]


def test_create_permutation():
    first_result_set = [{'a': 1}, {'a': 2}, {'a': 3}]
    second_result_set = [{'b': 1}, {'b': 2}]
    third_result_set = [{'c': 1}]
    EXAMPLES_PER_TEMPLATE = 3
    get_best_matches = lambda x: x

    single_result_set = generator.create_permutation([first_result_set], get_best_matches, ['a'], EXAMPLES_PER_TEMPLATE)
    assert len(single_result_set) == 3
    assert single_result_set == first_result_set

    result = generator.create_permutation([first_result_set, second_result_set], get_best_matches, ['a', 'b'], EXAMPLES_PER_TEMPLATE)
    assert len(result) == 3
    assert {'a': 1, 'b': 1} in result
    assert {'a': 2, 'b': 2} in result
    assert {'a': 3, 'b': 1} in result

    result_three_set = generator.create_permutation([first_result_set, second_result_set, third_result_set], get_best_matches, ['a', 'b', 'c'], EXAMPLES_PER_TEMPLATE)
    assert len(result_three_set) == 3
    assert {'a': 1, 'b': 1, 'c': 1} in result_three_set
    assert {'a': 2, 'b': 2, 'c': 1} in result_three_set
    assert {'a': 3, 'b': 1, 'c': 1} in result_three_set