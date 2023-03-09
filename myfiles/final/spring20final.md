# 1a

def points_off(days):
    return 100 - pow(2, days)

if __name__ == '__main__':
    print(points_off(4))

# 1b

# 2a

if you made a branch off and edited the file with the exact same code that someone on the original branch edited his/her code with, aka same changes, then both of you guys committed. if you merged, you'd look at the two commits as identical. but, they would have different hashes.

# 2b

no, it wouldnt make sense because you shouldn't version control anything in the .git directory. that stuff is local to ur repository. if 2 ppl clone from the same remote, change their remotes, they shud be able to push it back without having conflict. 

# 3

N/A

# 4

no, it wouldnt make sense for an HTML document to be in the format of a DAG. in the format of an HTML document, the body is the root of the tree, and there might be multiple divs that are the children of "body." in a tree, this makes sense. each div can then branch out into multiple headers, and paragraphs. However, if this was in the shape of a DAG, the divs can connect to each other? which makes no sense.

# 5a

no, it wouldnt make sense. merges wouldn't be able to happen. a tree is essentially a undirected acyclic graph, and therefore no loops at all would be allowed. if A branched to B1 and C1 and were edited to B100 and C100, they can't merge B100 and C100 back to A100 because theres a loop and that's not a tree

# 5b



