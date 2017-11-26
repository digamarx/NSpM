import csv

import collections


def read_questions (questionFile):
    used_resources = collections.Counter()
    with open(questionFile) as file:
        csv_reader = csv.reader(file, delimiter=':')
        for i, row in enumerate(csv_reader):
            instance = row[1] + str(i)
            number = int(str.strip(row[-1]))
            used_resources.update({instance: number})
    return used_resources

def log_statistics ( used_resources ):
    total_number_of_resources = len(used_resources)
    total_number_of_filled_placeholder_positions = sum(used_resources.values())
    examples_per_instance = collections.Counter()
    for resource in used_resources:
        count = used_resources[resource]
        examples_per_instance.update([count])

    print '{:6d} used resources in {} placeholder positions'.format(total_number_of_resources, total_number_of_filled_placeholder_positions)
    for usage in examples_per_instance:
        print '{:6d} resources occur \t{:6d} times \t({:6.2f} %) '.format(examples_per_instance[usage], usage, examples_per_instance[usage]*100/total_number_of_resources)

if __name__ == '__main__':
    used_res = read_questions('used_resources_2017-11-14-15-45.json_ml')
    log_statistics(used_res)