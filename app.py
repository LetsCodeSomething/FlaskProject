from flask import Flask

app = Flask(__name__)
app.secret_key = ""

import controllers.index
import controllers.posts
import controllers.login
import controllers.register
import controllers.profile
import controllers.remove_profile
import controllers.save_image
import controllers.remove_image
import controllers.create_post
import controllers.edit_post
import controllers.read_post
import controllers.remove_post