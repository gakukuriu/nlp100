import sys, json, numpy

with open(sys.argv[1], 'r') as feature:
    ids = json.load(feature)
    weight = numpy.load(sys.argv[2])
    sort_weight = numpy.sort(weight)
    sort_weight_desc = sort_weight[::-1]
    sort_index = numpy.argsort(weight)
    sort_index_desc = sort_index[::-1]
    ids_inv = {v:k for k, v in ids.items()}

    print('--------- Top 10 ---------')
    for i in range(10):
        print(ids_inv[sort_index_desc[i]], sort_weight_desc[i])

    print('--------- Worst 10 ---------')
    for i in range(10):
        print(ids_inv[sort_index[i]], sort_weight[i])
