import flask
import requests

app = flask.Flask(__name__)

@app.get("/")
def index():
    info = get_random_cat_info()
    return flask.render_template("cat_images_homepage.html",
                                 id=info.get("id"),
                                 image_url=info.get("url"),
                                 description=info.get("description"))

@app.get("/<id>")
def find_cat_by_id(id):
    info = get_cat_info(id)
    return flask.render_template("cat_images_homepage.html",
                                 id=info.get("id"),
                                 image_url=info.get("url"),
                                 description=info.get("description"))

def get_random_cat_info():
    try:
        search_res = requests.get("https://api.thecatapi.com/v1/images/search?limit=1", verify=False)
        id = search_res.json()[0]["id"]
        return get_cat_info(id)
    except:
        return {
            "description": "Unable to search for cats at this time"
        }

def get_cat_info(id):
    try:
        info_res = requests.get(f"https://api.thecatapi.com/v1/images/{id}", verify=False)
        return info_res.json()
    except:
        return {
            "description": "Unable to get this cat at this time"
        }


app.run(debug=True)
