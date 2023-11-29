def solution(l):
    new_lst = list()
    output = list()
    for version in l:
        new_lst.append([int(item) for item in version.split(".")])

    for version in sorted(new_lst):
        output.append(".".join([str(item) for item in version]))
    return output
