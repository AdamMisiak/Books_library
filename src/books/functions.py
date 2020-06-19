from goodreads import client


key = 'FEUyDOTJtyNhRRSmYMw'
secret = 'A5kisVJMF6LvMMJiIlSc7BfhSJTrRN719v6zpFoN0'

gc = client.GoodreadsClient(key, secret)


def books_finder(title):
	book_dict = {}
	result_list = []
	books = gc.search_books(title)

	for index, book in enumerate(books):
		id = book.gid
		title = book.title
		author = book.authors[0]
		description = book.description
		image = book.image_url

		book_dict['id'] = id
		book_dict['title'] = title
		book_dict['author'] = author
		book_dict['image'] = image
		book_dict['description'] = description

		result_list.append(book_dict)
		book_dict = {}
	return result_list


