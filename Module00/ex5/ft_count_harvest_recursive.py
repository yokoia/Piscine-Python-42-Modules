def ft_count_harvest_recursive():
    def ft_counting(i, days):
        print("Day", i)
        if i < days:
            ft_counting(i + 1, days)
    days = int(input("Days until harvest: "))
    i = 1
    ft_counting(i, days)
    print("Harvest time!")
