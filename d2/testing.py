with open('d2/inputs_sample.txt', 'r') as f:
    inputs_sample = []
    for line in f.readlines():
        line_trimmed_and_splitted = line.strip('\n').split(' ')
        tuple_line_trimmed = tuple(line_trimmed_and_splitted)
        inputs_sample.append()

print(inputs_sample)