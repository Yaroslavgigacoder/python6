def choose_coffee(*preference):
    ingredients = [2, 3, 2]
    print(ingredients)
    for i in range(len(preference)):
        if preference[i] == 'Эспрессо':
            if ingredients[0] >= 1:
                return print('Эспрессо')
        elif preference[i] == 'Капучино':
            if ingredients[0] >= 1 and ingredients[1] >= 3:
                return print('Капучино')
        elif preference[i] == 'Маккиато':
            if ingredients[0] >= 2 and ingredients[1] >= 1:
                return print('Маккиато')
        elif preference[i] == 'Кофе-по-венски':
            if ingredients[0] >= 1 and ingredients[2] >= 2:
                return print('Кофе по-венски')
        elif preference[i] == 'Латте Маккиато':
            if ingredients[0] >= 1 and ingredients[1] >= 2 and ingredients[2] >= 1:
                return print('Латте Маккиато')
        elif preference[i] == 'Кон Панна':
            if ingredients[0] >= 1 and ingredients[2] >= 1:
                return print('Кон Панна')
    return ('К сожалению, не можем предложить Вам напиток')
