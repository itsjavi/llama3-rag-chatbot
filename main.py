from app import app
import config

if __name__ == '__main__':
    app.config.from_object(config.Config)
    app.run(debug=config.Config.DEBUG)
