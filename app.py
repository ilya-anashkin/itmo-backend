import time
from db import database
from flask import Flask, request, make_response, jsonify
from http import HTTPStatus
from sqlalchemy.orm import Session

app = Flask(__name__)
database.Base.metadata.drop_all(database.engine)
database.Base.metadata.create_all(database.engine)


@app.post("/api/directors")
def create_director():
    try:
        data = request.json
        director_data = data["director"]

        if len(director_data["fio"]) > 100:
            raise ValueError("Length of field 'fio' should be less then 100")

        director = database.Director(id=director_data["id"], fio=director_data["fio"])

        with Session(database.engine) as session:
            session.add(director)
            session.commit()

        return data
    except (KeyError, ValueError) as ex:
        return make_response(
            jsonify({"status": HTTPStatus.BAD_REQUEST, "reason": str(ex)}),
            HTTPStatus.BAD_REQUEST,
        )
    except Exception as ex:
        return make_response(
            jsonify({"status": HTTPStatus.INTERNAL_SERVER_ERROR, "reason": str(ex)}),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )


@app.get("/api/directors/<director_id>")
def get_director(director_id):
    try:
        director = None
        with Session(database.engine) as session:
            director = (
                session.query(database.Director)
                .where(database.Director.id == director_id)
                .first()
            )
            if not director:
                return make_response("", HTTPStatus.NOT_FOUND)

        return make_response(
            jsonify(
                {
                    "director": {"id": director.id, "fio": director.fio},
                }
            ),
            HTTPStatus.OK,
        )
    except Exception as ex:
        return make_response(
            jsonify({"status": HTTPStatus.INTERNAL_SERVER_ERROR, "reason": str(ex)}),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )


@app.get("/api/directors")
def get_directors():
    try:
        directors = None
        with Session(database.engine) as session:
            directors = session.query(database.Director).all()

        return make_response(
            jsonify(
                {
                    "list": [
                        {"id": director.id, "fio": director.fio}
                        for director in directors
                    ],
                }
            ),
            HTTPStatus.OK,
        )
    except Exception as ex:
        return make_response(
            jsonify({"status": HTTPStatus.INTERNAL_SERVER_ERROR, "reason": str(ex)}),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )


@app.patch("/api/directors/<director_id>")
def patch_director(director_id):
    try:
        data = request.json
        director_data = data["director"]

        if len(director_data["fio"]) > 100:
            raise ValueError("Length of field 'fio' should be less then 100")

        with Session(database.engine) as session:
            director = (
                session.query(database.Director)
                .where(database.Director.id == director_id)
                .first()
            )
            if not director:
                return make_response("", HTTPStatus.NOT_FOUND)

            director.id = director_data["id"]
            director.fio = director_data["fio"]
            session.commit()

        return make_response(jsonify(data), HTTPStatus.OK)
    except (KeyError, ValueError) as ex:
        return make_response(
            jsonify({"status": HTTPStatus.BAD_REQUEST, "reason": str(ex)}),
            HTTPStatus.BAD_REQUEST,
        )
    except Exception as ex:
        return make_response(
            jsonify({"status": HTTPStatus.INTERNAL_SERVER_ERROR, "reason": str(ex)}),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )


@app.delete("/api/directors/<director_id>")
def delete_director(director_id):
    try:
        with Session(database.engine) as session:
            director = (
                session.query(database.Director)
                .where(database.Director.id == director_id)
                .first()
            )
            if not director:
                return make_response("", HTTPStatus.NOT_FOUND)

            session.delete(director)
            session.commit()

        return make_response("", HTTPStatus.ACCEPTED)
    except Exception as ex:
        return make_response(
            jsonify({"status": HTTPStatus.INTERNAL_SERVER_ERROR, "reason": str(ex)}),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )


@app.post("/api/movies")
def create_movie():
    try:
        data = request.json
        movie_data = data["movie"]

        if len(movie_data["title"]) > 100:
            raise ValueError("Length of field 'title' should be less then 100")

        if movie_data["year"] < 1900 or movie_data["year"] > 2100:
            raise ValueError("Field 'year' should be in [1900, 2100]")

        if movie_data["rating"] < 0 or movie_data["rating"] > 10:
            raise ValueError("Field 'rating' should be in [0, 10]")
        
        try:
            time.strptime(movie_data['length'], '%H:%M:%S')
        except:
            raise ValueError("Field 'length' should be '%H:%M:%S' format")

        movie = database.Movie(
            id=movie_data["id"],
            title=movie_data["title"],
            year=movie_data["year"],
            director_id=movie_data["director"],
            length=movie_data["length"],
            rating=movie_data["rating"],
        )

        with Session(database.engine) as session:
            session.add(movie)
            session.commit()

        return data
    except (KeyError, ValueError) as ex:
        return make_response(
            jsonify({"status": HTTPStatus.BAD_REQUEST, "reason": str(ex)}),
            HTTPStatus.BAD_REQUEST,
        )
    except Exception as ex:
        return make_response(
            jsonify({"status": HTTPStatus.INTERNAL_SERVER_ERROR, "reason": str(ex)}),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )


@app.get("/api/movies/<movie_id>")
def get_movie(movie_id):
    try:
        movie = None
        with Session(database.engine) as session:
            movie = (
                session.query(database.Movie)
                .where(database.Movie.id == movie_id)
                .first()
            )
            if not movie:
                return make_response("", HTTPStatus.NOT_FOUND)

        return make_response(
            jsonify(
                {
                    "movie": {
                        "id": movie.id,
                        "title": movie.title,
                        "year": movie.year,
                        "director": movie.director_id,
                        "length": movie.length,
                        "rating": movie.rating,
                    },
                }
            ),
            HTTPStatus.OK,
        )
    except Exception as ex:
        return make_response(
            jsonify({"status": HTTPStatus.INTERNAL_SERVER_ERROR, "reason": str(ex)}),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )


@app.get("/api/movies")
def get_movies():
    try:
        movies = None
        with Session(database.engine) as session:
            movies = session.query(database.Movie).all()

        return make_response(
            jsonify(
                {
                    "list": [
                        {
                            "id": movie.id,
                            "title": movie.title,
                            "year": movie.year,
                            "director": movie.director_id,
                            "length": movie.length,
                            "rating": movie.rating,
                        }
                        for movie in movies
                    ],
                }
            ),
            HTTPStatus.OK,
        )
    except Exception as ex:
        return make_response(
            jsonify({"status": HTTPStatus.INTERNAL_SERVER_ERROR, "reason": str(ex)}),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )


@app.patch("/api/movies/<movie_id>")
def patch_movie(movie_id):
    try:
        data = request.json
        movie_data = data["movie"]

        with Session(database.engine) as session:
            movie = (
                session.query(database.Movie)
                .where(database.Movie.id == movie_id)
                .first()
            )
            if not movie:
                return make_response("", HTTPStatus.NOT_FOUND)

            movie.id = movie_data["id"]
            movie.title = movie_data["title"]
            movie.year = movie_data["year"]
            movie.director_id = movie_data["director"]
            movie.length = movie_data["length"]
            movie.rating = movie_data["rating"]

            session.commit()

        return make_response(jsonify(data), HTTPStatus.OK)
    except (KeyError, ValueError) as ex:
        return make_response(
            jsonify({"status": HTTPStatus.BAD_REQUEST, "reason": str(ex)}),
            HTTPStatus.BAD_REQUEST,
        )
    except Exception as ex:
        return make_response(
            jsonify({"status": HTTPStatus.INTERNAL_SERVER_ERROR, "reason": str(ex)}),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )


@app.delete("/api/movies/<movie_id>")
def delete_movie(movie_id):
    try:
        with Session(database.engine) as session:
            movie = (
                session.query(database.Movie)
                .where(database.Movie.id == movie_id)
                .first()
            )
            if not movie:
                return make_response("", HTTPStatus.NOT_FOUND)

            session.delete(movie)
            session.commit()

        return make_response("", HTTPStatus.ACCEPTED)
    except Exception as ex:
        return make_response(
            jsonify({"status": HTTPStatus.INTERNAL_SERVER_ERROR, "reason": str(ex)}),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )
