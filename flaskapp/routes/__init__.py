"""
routes
======

Each file in this package will correspond to a single route
"""

from routes import (
    # list files by name, without extension
    hello
)


def register_views(app):
    """Register the blueprints using the app object"""
    app.register_blueprint(hello.bp)
#end register_views
