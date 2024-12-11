from typing import List, Tuple, Optional

def check_against_rule(rules: List[Tuple[int, int]], a: int, b: int) -> bool:
    for rule in rules:
        if rule[0] == a and rule[1] == b:
            return True
    return False

def check_page_order(rules: List[Tuple[int, int]], pages: List[List[int]]) -> bool:
    for page_no in range(0, len(pages)-1):
        for page_no_2 in range(page_no + 1, len(pages)):
            if not check_against_rule(rules, pages[page_no], pages[page_no_2]):
                return False
    return True

def reorder_pages(rules: List[Tuple[int, int]], pages: List[int]) -> Optional[List[int]]:
    reordered: List[int] = pages.copy()
    while not check_page_order(rules, reordered):
        for i in range(0, len(reordered) - 1):
            if not check_against_rule(rules, reordered[i], reordered[i + 1]):
                reordered[i], reordered[i + 1] = reordered[i + 1], reordered[i]
    return reordered

if __name__ == '__main__':
    from utils import read_data_file
    rules_txt = read_data_file('../data/day_5/sample_data.txt')
    rules: List[Tuple[int, int]] = []
    pages_list: List[List[int]] = []
    before_separator: bool = True
    for line in rules_txt:
        if line == '':
            before_separator = False
        else:
            if before_separator:
                line_data = line.split('|')
                rules.append((int(line_data[0]), int(line_data[1])))
            else:
                pages_list.append([int(x) for x in line.split(',')])
    
    sum_middle = 0
    sum_middle2 = 0
    for pages in pages_list:
        pages_ok = check_page_order(rules, pages)
        if pages_ok:
            sum_middle += pages[len(pages) // 2]
        else:
            reordered_pages = reorder_pages(rules, pages)
            sum_middle2 += reordered_pages[len(reordered_pages) // 2]
    print(sum_middle)
    print(sum_middle2)