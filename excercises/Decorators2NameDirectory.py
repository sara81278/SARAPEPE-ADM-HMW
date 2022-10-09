

def person_lister(f):
    def inner(people):
        people = sorted(people, key = lambda x: int(x[2]))
        outputList = list(map(f, people))
        return outputList
    return inner

