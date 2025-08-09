from flask import Flask, render_template
from flask_restful import Api
from resources.recipe import RecipeListResource, RecipeResource, RecipePublishResource

app = Flask(__name__)
api = Api(app)

api.add_resource(RecipeListResource, '/recipes')
api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
api.add_resource(RecipePublishResource, '/recipes/<int:recipe_id>/publish')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")
