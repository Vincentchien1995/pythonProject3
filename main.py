def simple_search(tab, item):
    i = 0
    while i < len(tab):
        if tab[i] == item:
            return i
        i += 1
        return -1

nitems = int(input("Enter the number of items: "))
items = []
i = 0
while i < nitems:
    item = float(input("Enter the item: "))
    items.append(item)
    i += 1

print(simple_search(items,4))
