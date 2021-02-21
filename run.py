from app import app_builder

app_builder.run(
    host=app_builder.config["APP_HOST"],
    port=app_builder.config["APP_PORT"],
    debug=app_builder.config["APP_DEBUG"]
)