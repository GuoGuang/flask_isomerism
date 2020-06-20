from flask import Blueprint, render_template
from models.movie import Movie
import json

index_page = Blueprint("index_page", __name__)


@index_page.route('/movie', methods=["GET"])
def query_all():
    items = []
    rows = Movie.query.all()
    for row in rows:
        items.append(row.to_dict())
    return json.dumps(items, ensure_ascii=False)


@index_page.route('/movie/<id>', methods=["GET"])
def query_condition(id):
    row = Movie.query.filter_by(id=id).first()
    print(row)
    return json.dumps(row.to_dict(), ensure_ascii=False)
