   
def find_fav(objects_from_db, searching_field):
    temp_dict = {}
    # FINDING THE FAV GENRE
    if searching_field == 'genre':
        for element in objects_from_db:
            if element.book.genre_1 in temp_dict.keys():
                temp_dict[element.book.genre_1] += 1
            elif element.book.genre_1 != '':
                temp_dict[element.book.genre_1] = 1
        return max(temp_dict, key= lambda x: temp_dict[x])
    # FINDING THE FAV GENRE
    elif searching_field == 'month':
        for element in objects_from_db:
            if element.month in temp_dict.keys():
                temp_dict[element.month] += 1
            elif element.month != '':
                temp_dict[element.month] = 1
        return max(temp_dict, key= lambda x: temp_dict[x])