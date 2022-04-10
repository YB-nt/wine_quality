from flask import Flask 

def create_app(config=None):
    app = Flask(__name__)
    
    if config is not None:
            app.config.update(config)

    from application.views.main import main
    from application.views.result import result
    app.register_blueprint(main)
    app.register_blueprint(result)

    return app

if __name__ =="__main__":
    app = create_app()
    app.run(debug=True)