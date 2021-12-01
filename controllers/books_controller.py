from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from models.book import Book 
from repositories import book_repository
from repositories import author_repository
from models.author import Author
from flask import Blueprint

books_blueprint = Blueprint("book", __name__)

@books_blueprint.route("/books")
def all_books():
    books=book_repository.select_all()
    return render_template("books/index.html",books=books)

@books_blueprint.route("/books/new")
def new_task():
    authors=author_repository.select_all()
    return render_template("books/new.html",authors=authors)