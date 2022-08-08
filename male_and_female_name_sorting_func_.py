def name_sorter(name_list):
    name_dict = {
        'male': [],
        'female': []
    }
    for name in name_list:
        if name[-1]== "a":
            name_dict['female'].append(name)
        else:
            name_dict['male'].append(name)
    return name_dict

names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
print(name_sorter(names))
