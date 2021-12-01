with open('input.txt', 'r') as inputFile:
    lines = inputFile.readlines()

depths = list(map(int, lines))
depth_pairs = zip(depths, depths[1:])

increases_count = sum(map(lambda depth_pair: 1 if depth_pair[0] < depth_pair[1] else 0, depth_pairs))

print(f"Part 1: {increases_count}")

depth_triples = list(zip(depths, depths[1:], depths[2:]))
depth_triple_pairs = zip(depth_triples, depth_triples[1:])

increases_count = sum(map(lambda depth_triple_pair: 1 if sum(depth_triple_pair[0]) < sum(depth_triple_pair[1]) else 0,
                          depth_triple_pairs))

print(f"Part 2: {increases_count}")