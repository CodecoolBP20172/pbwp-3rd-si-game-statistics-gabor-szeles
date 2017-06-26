import math
from collections import OrderedDict


# builds a two-dimensional list using the given source file
def build_database(file_name):
    with open(file_name) as source:
        lines = source.read().split("\n")
        database = []
        for line in lines:
            line = line.split("\t")
            database.append(line)
        database_clean = []
        for data in database:  # if there are empty lines, there will be lists with a single string in the result list
            if data != [""]:   # this loop fixes this problem
                database_clean.append(data)
        return database_clean


# returns the title of the game with the most copies sold
def get_most_played(file_name):
    database = build_database(file_name)
    copies_sold = []
    for data in database:
        copies_sold.append(float(data[1]))
    for data in database:
        if float(data[1]) == max(copies_sold):
            return data[0]
            break


# returns the amount of copies sold total
def sum_sold(file_name):
    database = build_database(file_name)
    copies_sold = []
    for data in database:
        copies_sold.append(float(data[1]))
    return sum(copies_sold)


# returns the average selling of the elements
def get_selling_avg(file_name):
    database = build_database(file_name)
    sum_copies = sum_sold(file_name)
    num_elements = len(database)
    return sum_copies/num_elements


# returns the character length of the longest title
def count_longest_title(file_name):
    database = build_database(file_name)
    titles = []
    for data in database:
        titles.append(data[0])
    return len(max(titles, key=len))


# returns the average of the release dates, rounded up
def get_date_avg(file_name):
    database = build_database(file_name)
    release_years = []
    for data in database:
        release_years.append(int(data[2]))
    sum_of_years = sum(release_years)
    num_elements = len(database)
    return math.ceil(sum_of_years/num_elements)


# returns the properties of the given title as a list
def get_game(file_name, title):
    database = build_database(file_name)
    for data in database:
        if title == data[0]:
            data.insert(1, float(data[1]))  # Frankly I hate doing this but string numbers don't pass the test
            del data[2]
            data.insert(2, int(data[2]))
            del data[3]
            return data


# returns a dictionary where each genre is associated with the count of the games of its genre
def count_grouped_by_genre(file_name):
    database = build_database(file_name)
    genres = []
    genre_dict = {}
    for data in database:
        if data[3] not in genres:
            genres.append(data[3])
    for genre in genres:
        if genre not in genre_dict.keys():
            genre_dict.update({genre: 0})
        for data in database:
            if genre == data[3]:
                genre_dict[genre] += 1
    return genre_dict


# returns the the date ordered list of the titles in descending order
def get_date_ordered(file_name):
    database = build_database(file_name)
    year_dict = {}
    for data in database:
        year_dict.update({data[0]: int(data[2])})
    sorted_years = OrderedDict(sorted(year_dict.items(), key=lambda x: (-x[1], x[0])))
    sorted_list = []
    for title, year in sorted_years.items():
        sorted_list.append(title)
    return sorted_list
