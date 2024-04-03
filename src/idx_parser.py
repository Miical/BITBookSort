import re

def extract_three_strings(input_string):
    pattern = r'^([^/]+)(?:/([^/]+))?(?:/([^/]+))?$'
    match = re.match(pattern, input_string)
    return match.groups() if match else None

def erase_dot(s):
    return s if s is None else s.replace(".", "")

def parse_part(idx):
    pattern = r'^(?:[-=:(]?([a-zA-Z0-9.]+)\)?)' + r'(?:[-=:(]?([a-zA-Z0-9.]+)\)?)?' * 5 + r'$'
    match = re.match(pattern, idx)
    if match:
        group1, group2, group3, group4, group5, group6 = match.groups()
        return (erase_dot(group1), erase_dot(group2), erase_dot(group3), erase_dot(group4), erase_dot(group5), erase_dot(group6))
    else:
        return None

def parse_charnum(idx):
    pattern = r'[a-zA-Z]+|[0-9]+'
    matches = re.findall(pattern, idx)
    return matches

def parser(book_idx):
    # parse book_idx to three part, splited with '/'
    three_part = extract_three_strings(book_idx)
    if three_part is None:
        return None
    partA, partB, partC = three_part

    # parse three parts respectively
    partA_result, partB_result, partC_result = None, None, None
    if partA:
        partA_result = parse_part(partA)
        if partA_result is None:
            return None
    if partB:
        partB_result = parse_part(partB)
        if partB_result is None:
            return None
    if partC:
        partC_result = parse_part(partC)
        if partC_result is None:
            return None

    return (partA_result, partB_result, partC_result)

