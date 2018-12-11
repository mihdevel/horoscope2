from bottle import route, run, view
from horoscope import generate_prophecies


@route("/api/forecasts")
def index():
    return {
        "predictions": generate_prophecies(total_num=6, num_sentences=2)
    }


@route("/api/test")
def api_test():
    return {"test_passed": True}


run(
    host="localhost",
    port=8080,
    autoreload=True
)
