from flask import Flask


def create_app():
    """Create app.

    Returns:
        app.
    """
    app = Flask(__name__)

 
    with app.app_context():

        from .web import (
           test
        )

        app.register_blueprint(test.test_bp)
        return app


app = create_app()

if __name__ == "__main__":
    app.run()