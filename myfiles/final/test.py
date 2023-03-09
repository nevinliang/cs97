def is_tree(commit_set):
    v = set()
    q = []
    root = commit_set[0]

    q.append(commit_set[0])
    while len(q) != 0:
        top = q.pop()
        if top in v:
            return falsed
        v.add(top)
        for i in v.