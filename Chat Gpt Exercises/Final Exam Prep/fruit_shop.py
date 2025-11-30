fruits = {
'banana': 2.50,
'apple': 1.20,
'orange': 0.85,
'grapefruit': 1.45,
'kiwi':2.70,
'pineapple': 5.50,
'grapes': 3.85,
}

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekends = ['Saturday', 'Sunday']
def parse_line(fruit_name:str, week_day:str, quantity:float):
    errors = {}
    if fruit_name not in fruits:
        errors['fruit_name'] = f'{fruit_name} not found'
    if week_day not in weekdays and week_day not in weekends:
        errors['week_day'] = f'{week_day} invalid "day"'

    final_price = 0
    if fruit_name in fruits:
        if week_day in weekdays:
            final_price = fruits[fruit_name] * quantity
        elif week_day in weekends:
            final_price = (fruits[fruit_name] * 1.20) * quantity

    if errors:
        return errors
    else:
        return final_price

test = parse_line('apple', 'Sunday', 2)
print(test)



