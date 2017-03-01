# Form in flask

Tried creating form for flask app, here is the workflow.

* Create a forms.py file and create form with all its fields
* Create a template for rendering the form
* Create a view for handing the form.

### Prerequisites

* Install the required packages

```
pip install -r requirements.txt
```

### Run the App

* Create the database and populate it.

```
python db_create_users.py
```

* start the app

```
python run.py
```

* view the user and email-id 

```
http://localhost:5000/listUser
```

### TODO
* Work on adding support for migrations
* Explore the docs
* Try changing the migration code
