from flask import Blueprint, request, jsonify, render_template, redirect, url_for
import requests

main = Blueprint('main', __name__)

books = [] # Lưu dữ liệu sách

@main.route('/')
def index():
    return render_template('books.html', books=books)

@main.route("/add", methods=["POST"])
def add_book():
    formData = request.form
    
    new_book = {
        "id": formData["id"],
        "name": formData["name"],
        "quantity": int(formData["quantity"])
    }
    
    books.append(new_book)

    return redirect(url_for("main.index"))

@main.route("/delete/<book_id>", methods=["GET"])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
   
    return redirect(url_for("main.index"))


@main.route("/edit/<book_id>", methods=["POST"])
def edit_book(book_id):
    formData = request.form
    
    for item in books:
        if item["id"] == book_id:
            item["name"] = formData["name"]
            item["quantity"] = int(formData["quantity"])
            break

    return redirect(url_for("main.index"))