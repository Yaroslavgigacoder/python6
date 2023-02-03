def choose_coffee(*preference):
    ingredients = [4, 4, 0]
    print(ingredients)
    for i in range(len(preference)):
        if preference[i] == 'Эспрессо':
            if ingredients[0] >= 1:
                print('Эспрессо')
        if preference[i] == 'Капучино':
            if ingredients[0] >= 1 and ingredients[1] >= 3:
                print('Капучино')
        if preference[i] == 'Маккиато':
            if ingredients[0] >= 2 and ingredients[1] >= 1:
                print('Маккиато')
        if preference[i] == 'Кофе-по-венски':
            if ingredients[0] >= 1 and ingredients[2] >= 2:
                print('Кофе по-венски')
        if preference[i] == 'Латте Маккиато':
            if ingredients[0] >= 1 and ingredients[1] >= 2 and ingredients[2] >= 1:
                print('Латте Маккиато')
        if preference[i] == 'Кон Панна':
            if ingredients[0] >= 1 and ingredients[2] >= 1:
                print('Кон Панна')
    return ('К сожалению, не можем предложить Вам напиток')

# coffe = input().split(', ')

print(choose_coffee('Эспрессо','Маккиато', 'Капучино'))