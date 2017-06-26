import reports


test1 = reports.get_most_played("game_stat.txt")
print(test1)
test2 = reports.sum_sold("game_stat.txt")
print(test2)
test3 = reports.get_selling_avg("game_stat.txt")
print(test3)
test4 = reports.count_longest_title("game_stat.txt")
print(test4)
test5 = reports.get_date_avg("game_stat.txt")
print(test5)
test6 = reports.get_game("game_stat.txt", "World of Warcraft")
print(test6)
test7 = reports.count_grouped_by_genre("game_stat.txt")
print(test7)
test8 = reports.get_date_ordered("game_stat.txt")
print(test8)
# Printing functions
