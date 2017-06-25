# builds a two-dimensional list using the given source file
def build_database(file_name):
    with open(file_name) as source:
        lines = source.read().split("\n")
        database = []
        for line in lines:
            line = line.split("\t")
            database.append(line)
        del database[-1]  # last line is always empty therefore the last list would be empty as well
        return database


# counts games (basically the lines) in the given source
def count_games(file_name):
    with open(file_name) as source:
        lines = -1  # starts at -1 in case the file happens to be empty
        for lines, item in enumerate(source):
            pass
    return lines + 1


# decides if there is a game from the given year in the source
def decide(file_name, year):
    database = build_database(file_name)
    years = []
    for data in database:
        years.append(data[2])
    if str(year) in years:
        return True


# returns the title of the latest game_stat
def get_latest(file_name):
    database = build_database(file_name)
    years = []
    for data in database:
        years.append(data[2])
    max_year = max(years)
    for data in database:
        if data[2] == max_year:
            return data[0]
            break


# counts the number of games in the given genre
def count_by_genre(file_name, genre):
    database = build_database(file_name)
    genres = []
    for data in database:
        genres.append(data[3])
    count = 0
    for item in genres:
        if item == genre:
            count += 1
    return count


#  returns the line number of the given title
def get_line_number_by_title(file_name, title):
    database = build_database(file_name)
    titles = []
    for data in database:
        titles.append(data[0])
    if title not in titles:
        raise ValueError("Title not in database!")
    else:
        return titles.index(title)+1


# sorts titles alphabetically, returns a list
def sort_abc(file_name):
    database = build_database(file_name)
    titles = []
    for data in database:
        titles.append(data[0])
    return sorted(titles)


# returns an alphabetically sorted list of genres
def get_genres(file_name):
    database = build_database(file_name)
    genres = []
    for data in database:
        if data[3] not in genres:
            genres.append(data[3])
    return sorted(genres, key=lambda v: v.upper())


# returns the release date of the top-sold FPS title
def when_was_top_sold_fps(file_name):
    database = build_database(file_name)
    copies_sold = []
    for data in database:
        if data[3] == "First-person shooter":
            copies_sold.append(float(data[1]))
    for data in database:
        if max(copies_sold) == float(data[1]):
            return int(data[2])
