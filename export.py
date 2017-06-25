import reports


# exports results into a text file
def export_results(filename="results.txt"):
    with open(filename, "w") as export_file:
        export_file.write(str(reports.count_games("game_stat.txt"))+"\n")
        export_file.write(str(reports.decide("game_stat.txt", 1970))+"\n")
        export_file.write(str(reports.get_latest("game_stat.txt"))+"\n")
        export_file.write(str(reports.count_by_genre("game_stat.txt", "Survival game"))+"\n")
        export_file.write(str(reports.get_line_number_by_title("game_stat.txt", "World of Warcraft"))+"\n")
        export_file.write(str(reports.sort_abc("game_stat.txt"))+"\n")
        export_file.write(str(reports.get_genres("game_stat.txt"))+"\n")
        export_file.write(str(reports.when_was_top_sold_fps("game_stat.txt"))+"\n")


export_results()
