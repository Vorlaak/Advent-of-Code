import re

def get_input() :
    #return("example.txt")
    return("input.txt")

def get_rules(text) :
    pattern = r'(?s)(.*?)(?:\r*\n){2}'
    rules = []
    with open(text, 'r') as file :
        data = file.read()
        list_of_rules = re.findall(pattern, data)[0].split('\n')
        for rule in list_of_rules :
            pages = rule.split('|')
            rules.append((int(pages[0]), int(pages[1])))
    return rules

def get_updates(text) :
    pattern = r'(?s)(?<=\n{2}).*'
    updates = []
    with open(text, 'r') as file :
        data = file.read()
        list_of_updates = re.findall(pattern, data)[0].split('\n')
        for update in list_of_updates :
            pages = update.split(',')
            pages_list = []
            for page in pages :
                pages_list.append(int(page))
            updates.append(pages_list)
    return updates


def check_rule(update, rule) :
    (page_1, page_2) = rule
    check = True
    flag = True
    if page_1 in update :
        for page in update :
            if page == page_1 :
                check = False
            elif check and (page == page_2) :
                flag = False
    return flag

def check_rules(update, rules) :
    flag = True
    for rule in rules :
        if not check_rule(update, rule) :
            flag = False
    return flag

def main() :
    textfile = get_input()
    rules = get_rules(text=textfile)
    updates = get_updates(text=textfile)
    sum = 0
    for update in updates :
        if check_rules(update=update, rules=rules) :
            sum += update[len(update)//2]
    print(sum)

if __name__=="__main__":
    main()