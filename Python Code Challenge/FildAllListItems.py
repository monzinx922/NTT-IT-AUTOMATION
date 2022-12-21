# find list in list until no list
# need to find item position in multi dimension list
# define member in each level
# can I list all index position?
# can I check how many dimension of the list?
""" def find_item_index(item_list,x):
    i = 0
    for item in item_list:
        if type(item) != list:
            i.append(item)
        else:
            
    return 0

example = [[[1,2,3],2,[1,3]],[1,2,3]]
 """


def find_item_indexes(items, target, indexes=[]):
    result = []
    if isinstance(items, list):
        print("Found items is a list")
        print("items = ",items)
        for i, item in enumerate(items):
            print("put in recursive to check if it still have list in item")
            print("i = ",i)
            print("item = ",item)
            result.extend(find_item_indexes(item, target, indexes + [i]))
    elif items == target:
        print("item is not list and it is target then add the index")
        result.append(indexes)
        #print("result = ",result)
    print("result = ",result)
    return result

# items = [['apple', 'banana', 'orange'], ['mango', 'apple', 'pear'], ['grape', 'apple', 'plum']]
example = [[[1,2,3],2,[1,3]],[1,2,3]]
indexes = find_item_indexes(example, 2)
print("answer is ",indexes)
