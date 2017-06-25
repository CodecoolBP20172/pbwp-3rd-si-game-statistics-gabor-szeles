import reports

test1 = reports.count_games("game_stat.txt")
print(test1)
test2 = reports.decide("game_stat.txt", 1989)
print(test2)
test3 = reports.get_latest("game_stat.txt")
print(test3)
test4 = reports.count_by_genre("game_stat.txt", "Survival game")
print(test4)
test5 = reports.get_line_number_by_title("game_stat.txt", "World of Warcraft")
print(test5)
test6 = reports.sort_abc("game_stat.txt")
print(test6)
test7 = reports.get_genres("game_stat.txt")
print(test7)
test8 = reports.when_was_top_sold_fps("game_stat.txt")
print(test8)
# Printing functions
