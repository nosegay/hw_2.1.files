from pprint import pprint


def get_recipes(dish_list='all'):
    cook_book_file = 'recipes.txt'
    cook_book = dict()
    inner_dict_keys = ('ingredient_name', 'quantity', 'measure')
    with open(cook_book_file, 'r', encoding='utf8') as fp:
        while True:
            recipe_name = fp.readline().strip(' \r\n')

            if not recipe_name:
                break

            ingredient_ctr = int(fp.readline())

            if not dish_list == 'all' and recipe_name not in dish_list:
                for i in range(ingredient_ctr + 1):
                    fp.readline()

                continue

            cook_book[recipe_name] = list()
            for i in range(ingredient_ctr):
                name, measure, quantity = fp.readline().strip(' \n\r').split(' | ')
                cook_book[recipe_name].append(dict(zip(inner_dict_keys, (name, int(measure), quantity))))

            fp.readline()

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    dishes_list = get_recipes(dishes)

    shoping_list = dict()
    for dish in dishes_list.values():
        for ingredient in dish:
            if ingredient['ingredient_name'] not in shoping_list:
                shoping_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                            'quantity': ingredient['quantity'] * person_count}
            else:
                shoping_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count

    return shoping_list


if __name__ == '__main__':
    # print('Список доступных рецептов:')
    # pprint(get_recipes())

    print('Список покупок:')
    pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
