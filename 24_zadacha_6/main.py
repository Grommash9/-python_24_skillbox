from elements import Air, Water, Fire, Dirt, Meat

elements_list = [Air(), Water(), Fire(), Dirt(), Meat()]

for base_element in elements_list:
    for added_element in elements_list[::-1]:
        result = base_element + added_element
        print('Смешивая {base} с {added} мы получим {result}'.format(
            base=base_element.name,
            added=added_element.name,
            result=result.name
        ))
