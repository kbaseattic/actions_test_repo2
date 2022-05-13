from flask import Flask, render_template, request, jsonify
from datetime import datetime
import git
from os import path

git_url = "https://github.com/kbase/static-content.git"
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')


# Pull repo on get `/pull`
@app.route("/")
def pull():
  if path.exists('./static/index.html'):
    d = git.cmd.Git('static')
    d.pull()
    return "<p>Repo Updated!</p>"
  else:
    d = git.Repo.clone_from(git_url, 'static')
    return "<p>Repo Cloned!</p>"

# This route serves static/index.html at the route / and it's subpaths
# @app.route("/", defaults={"subpath": ""})
# @app.route("/<path:subpath>")
# def index(subpath):
#   if path.exists('./static'):
#     return app.send_static_file('index.html')
#   else:
#     d = git.Repo.clone_from(git_url, 'static')
#     return app.send_static_file('index.html')


if __name__ == "__main__":
  # app.config["TEMPLATES_AUTO_RELOAD"] = True
  app.run(debug=True, host='0.0.0.0')

    
