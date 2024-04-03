from idx_parser import *
from compare import bookidx_cmp
from functools import cmp_to_key
import openpyxl


workbook = openpyxl.load_workbook('../xlsx/booklist.xlsx')
sheet = workbook['总表']
target_column_name = 'G'
book_idxs = [cell.value for cell in sheet[target_column_name]][1:]
print("Load completed")

parse_success = []
parse_fail = []

for i in range(len(book_idxs)):
    result = parser(book_idxs[i])
    if result is not None:
        parse_success.append((i, book_idxs[i]))
    else:
        parse_fail.append((i, book_idxs[i]))

print("parsing completed")

print("The following book idx could not be resolved:")
for (row, book_idx) in parse_fail:
    print(f"line: {row}, book_idx: {book_idx}")

def key_func(item1, item2):
    return bookidx_cmp(item1[1], item2[1])

sorted_idxs = sorted(parse_success, key=cmp_to_key(key_func))

print(sorted_idxs)

