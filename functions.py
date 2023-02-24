def print_all():
    d = open('directory.txt', 'r', encoding='utf-8')
    print(d.read())
    d.close()

def find_entry(name):
    d = open('directory.txt', 'r', encoding='utf-8')
    #print(d)
    list_of_entries = list()
    for l in d:
        #print(l)
        if name in l.split():
            list_of_entries.append(l)
    d.close()
    return list_of_entries

def add_entry(data):
    d = open('directory.txt', 'a', encoding='utf-8')
    d.write(' '.join(data)+ '\n')
    d.close()
    
