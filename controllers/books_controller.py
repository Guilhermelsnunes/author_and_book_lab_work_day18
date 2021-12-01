from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from models.book import Book 
from repositories import book_repository
from repositories import author_repository
from models.author import Author
from flask import Blueprint

books_blueprint = Blueprint("book", __name__)
