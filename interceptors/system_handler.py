from config.env_config import app
from controllers.movie import index_page

from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension(app)

'''
拦截器处理 和 错误处理器
'''
from interceptors.errorHandler import *

app.register_blueprint(index_page, url_prefix="/api")


@app.after_request
def apply_caching(response):
    response.headers["Content-type"] = "application/json;charset=UTF-8"
    return response
