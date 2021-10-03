"""Hobbies."""


def sort_dictionary(dic: dict) -> dict:
    """Sort dictionary values alphabetically."""
    sorted_dic = {}
    for key in sorted(dic):
        sorted_dic[key] = sorted(dic[key])
    return sorted_dic


def create_dictionary(data: str) -> dict:
    """Create dictionary about people and their hobbies ie."""
    dic = {}
    pairs_data = data.split("\n")
    for pair in pairs_data:
        name, hobby = pair.split(':')
        if name not in dic:
            dic[name] = [hobby]
            dic[name].sort()
        if hobby not in dic[name]:
            dic[name].append(hobby)
            dic[name].sort()
    return dic


def create_dictionary_with_hobbies(data: str) -> dict:
    """Create dictionary about hobbies and their hobbyists ie."""
    dictionary = {}
    pairs_data = data.split("\n")
    for pair in pairs_data:
        name, hobby = pair.split(':')
        if hobby not in dictionary:
            dictionary[hobby] = [name]
        if name not in dictionary[hobby]:
            dictionary[hobby].append(name)

    return sort_dictionary(dictionary)


def find_people_with_most_hobbies(data: str) -> list:
    """Find the people who have most hobbies."""
    max_hobbies_list = []
    max_value = 0
    for value in create_dictionary(data).values():
        amount = len(value)
        if amount > max_value:
            max_value = amount
    for name, value in create_dictionary(data).items():
        if len(value) == max_value:
            max_hobbies_list.append(name)
            max_hobbies_list.sort()
    return max_hobbies_list


def find_people_with_least_hobbies(data: str) -> list:
    """Find the people who have least hobbies."""
    least_hobbies_list = []
    min_value = 0
    for value in create_dictionary(data).values():
        amount = len(value)
        min_value = amount
        if amount < min_value:
            min_value = amount
    for name, value in create_dictionary(data).items():
        if len(value) == min_value:
            least_hobbies_list.append(name)
            least_hobbies_list.sort()
    return least_hobbies_list


def find_most_popular_hobbies(data: str) -> list:
    """
    Find the most popular hobbies.

    :param data: given string from database
    :return: list of most popular hobbies. Sorted alphabetically.
    """
    most_pop_hobbies = []
    max_value = 0
    for value in create_dictionary_with_hobbies(data).values():
        amount = len(value)
        if amount > max_value:
            max_value = amount
    for name, value in create_dictionary_with_hobbies(data).items():
        if len(value) == max_value:
            most_pop_hobbies.append(name)
            most_pop_hobbies.sort()
    return most_pop_hobbies


def find_least_popular_hobbies(data: str) -> list:
    """Find the least popular hobbies."""
    least_pop_hobbies = []
    min_value = 10000000000
    for value in create_dictionary_with_hobbies(data).values():
        amount = len(value)
        if amount < min_value:
            min_value = amount
    for name, value in create_dictionary_with_hobbies(data).items():
        if len(value) == min_value:
            least_pop_hobbies.append(name)
            least_pop_hobbies.sort()
    return least_pop_hobbies


def sort_names_and_hobbies(data: str) -> tuple:
    """Create a tuple of sorted names and their hobbies."""
    lists = []
    for key, value in sorted(create_dictionary(data).items()):
        value = tuple(value)
        lists.append(tuple([key, value]))
    return tuple(lists)


if __name__ == '__main__':
    sample_data = """Jack:crafting\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""
    dic = create_dictionary(sample_data)
    print(find_people_with_most_hobbies(sample_data))  # -> ['Jack']
    print(len(dic["Jack"]))  # ->  12
    print(len(dic["Carmen"]))  # -> 10
    print(find_people_with_least_hobbies(sample_data))  # -> ['Molly']
    print(len(dic["Molly"]))  # -> 5
    print(len(dic["Sophie"]))  # -> 7
    print(find_most_popular_hobbies(sample_data))  # -> ['football', 'gaming', 'sport']
    print(find_least_popular_hobbies(sample_data))  # -> ['dance', 'flowers', 'puzzles', 'tennis']
    sort_result = sort_names_and_hobbies(sample_data)
    # if the condition after assert is False, error will be thrown.
    assert isinstance(sort_result, tuple)
    assert len(sort_result) == 10
    assert sort_result[0][0] == 'Alfred'
    assert len(sort_result[0][1]) == 7
    assert sort_result[-1] == ('Wendy', ('fishing', 'fitness', 'football', 'gaming', 'photography', 'puzzles', 'shopping', 'sport', 'theatre'))
    # if you see this line below, then everything seems to be ok!
    print("sorting works!")
