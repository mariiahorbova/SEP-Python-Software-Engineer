# 45. Написати программу, яка задає категорію та стаж працівника, а також ставку відповідно до категорії
# (1-ша категорія—3000, 2-га – 2000, 3-тя - - 1000). Обчислити заробітну плату, враховуючи надбавку за стаж роботи
# (до 2 років—0%, від 2 до 5 – 10%, від 5 до 10 – 20%, більше 10—30 % ) і зняття податку – 15%.

def salary(category, work_exp):
    categories = {1: 3000, 2: 2000, 3: 1000}
    inv_exp = "Invalid work experience"
    inv_cat = "Invalid category"
    if work_exp < 2:
        if category in categories.keys():
            return categories[category] * 0.85
        else:
            return inv_cat
    elif 2 <= work_exp < 5:
        if category in categories.keys():
            return categories[category] * 1.1 * 0.85
        else:
            return inv_cat
    elif 5 <= work_exp < 10:
        if category in categories.keys():
            return categories[category] * 1.2 * 0.85
        else:
            return inv_cat
    elif work_exp > 10:
        if category in categories.keys():
            return categories[category] * 1.3 * 0.85
        else:
            return inv_cat
    else:
        return inv_exp
    
    
    
print(salary(1, 12))
print(salary(3, 2))
print(salary(2, 7))
print(salary(4, 1))
