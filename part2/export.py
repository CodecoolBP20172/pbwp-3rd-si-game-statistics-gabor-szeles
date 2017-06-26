import reports


# exports results into a text file
def export_results(filename="results.txt"):
    with open(filename, "w") as export_file:
        export_file.write(str(reports.get_most_played("game_stat.txt"))+"\n")
        export_file.write(str(reports.sum_sold("game_stat.txt"))+"\n")
        export_file.write(str(reports.get_selling_avg("game_stat.txt"))+"\n")
        export_file.write(str(reports.count_longest_title("game_stat.txt"))+"\n")
        export_file.write(str(reports.get_date_avg("game_stat.txt"))+"\n")
        export_file.write(str(reports.get_game("game_stat.txt", "World of Warcraft"))+"\n")
        export_file.write(str(reports.count_grouped_by_genre("game_stat.txt"))+"\n")
        export_file.write(str(reports.get_date_ordered("game_stat.txt"))+"\n")


export_results()
# Export functions
