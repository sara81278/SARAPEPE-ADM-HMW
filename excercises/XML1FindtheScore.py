

def get_attr_number(node):
    return sum(len(el.attrib) for el in root.iter())

