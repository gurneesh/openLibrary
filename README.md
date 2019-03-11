<p align="center"><img src="app/static/img/horizontal.png" alt="BookLibrary" height="200px"></p>

# BookLibrary
Simple Book library application written on flask with SQLite database.

## Features
* user login, logout, register, change password, update about-me information
* user borrow/return books, write/delete comments
* administrator add/delete book, update book information
* administrator delete comments

## Screen Shot
Index page:
![index page](https://raw.githubusercontent.com/gurneesh/openLibrary/master/screenshots/1.png)

User detail page:
![user detail page](https://raw.githubusercontent.com/gurneesh/openLibrary/master/screenshots/2.png)

Book list page:
![book list page](https://raw.githubusercontent.com/gurneesh/openLibrary/master/screenshots/3.png)

Search Results Page:
![book detail page](https://raw.githubusercontent.com/gurneesh/openLibrary/master/screenshots/4.png)

## Installation
```sh
git clone https://github.com/hufan-Akari/BookLibrary.git
cd BookLibrary
virtualenv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
python ./run.py
```

Press CTRL+C to terminate the server.  
use `deactive` to quit the virtual environment.

## Dependencies

- [Flask](https://github.com/mitsuhiko/flask)
- [SQLAlchemy](https://github.com/zzzeek/sqlalchemy)
- [Flask-SQLAlchemy](https://github.com/mitsuhiko/flask-sqlalchemy)
- [Flask-Login](https://github.com/maxcountryman/flask-login)
- [Flask-WTF](https://github.com/lepture/flask-wtf)
- [Bootstrap](http://getbootstrap.com/)
- [Flask-Bootstrap](https://github.com/mbr/flask-bootstrap)
- [Markdown](https://pythonhosted.org/Markdown/)
- [Flask-PageDown](https://github.com/miguelgrinberg/Flask-PageDown)
- [Flask-Uploads](https://packages.python.org/Flask-Uploads/)
- [Bootstrap File Input](https://github.com/kartik-v/bootstrap-file-input)
