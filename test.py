from goodreads import client


key = 'FEUyDOTJtyNhRRSmYMw'
secret = 'A5kisVJMF6LvMMJiIlSc7BfhSJTrRN719v6zpFoN0'

gc = client.GoodreadsClient(key, secret)


def books_finder(title):
	books = gc.search_books(title)
	title = books[0]
	author = books[0].authors[0]
	description = books[0].description[:200]

	print(title)
	print(description)

books_finder('harry potter')