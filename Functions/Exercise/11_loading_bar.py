def loading_bar(number):
    progress_count = number // 10
    bar = '%' * progress_count + '.' * (10 - progress_count)

    if number == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    else:
        return f"{number}% [{bar}]\nStill loading..."

percentage = int(input())
print(loading_bar(percentage))
