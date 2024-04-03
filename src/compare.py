from idx_parser import parse_charnum, parser

def gen_comp_vec(parser_result):
    partA, partB, partC = parser_result
    partA = partA if partA is not None else [None] * 6
    partB = partB if partB is not None else [None] * 6
    partC = partC if partC is not None else [None] * 6

    comp_vec = []
    for part in [partA, partB, partC]:
        for i in range(6):
            comp_vec.append(part[i] if part[i] is not None else '!')

    return comp_vec

def single_charnum_comp(idx1, idx2):
    if idx1.isdigit() ^ idx2.isdigit():
        return idx1.isdigit()

    if idx1.isdigit():
        return int(idx1) < int(idx2)
    else:
        return idx1 < idx2

def charnumstr_comp(idx1, idx2):
    items1 = parse_charnum(idx1)
    items2 = parse_charnum(idx2)

    len1, len2 = len(items1), len(items2)
    min_len = min(len1, len2)
    for i in range(min_len):
        if items1[i] != items2[i]:
            return single_charnum_comp(items1[i], items2[i])
    return len1 < len2

def compvec_cmp(vec1, vec2):
    for val1, val2 in zip(vec1, vec2):
        if val1 != val2:
            return charnumstr_comp(val1, val2)
    return True

def bookidx_cmp(bookidx1, bookidx2):
    return compvec_cmp(
        gen_comp_vec(parser(bookidx1)),
        gen_comp_vec(parser(bookidx2))
    )

