from db.run_sql import run_sql

from models.author import Author
from models.book import Book

def select(id):
    author=None
    sql="SELECT * FROM authors WHERE id=%s"
    values=[id]
    result=run_sql(sql,values)[0]
    if result is not None:
        author=Author(result['name'],result['id'])
    return author

def select_all():
    authors=[]
    sql="SELECT * FROM authors"
    results=run_sql(sql)
    for row in results:
        author=Author(row['name'],row['id'])
        authors.append(author)
    return authors
