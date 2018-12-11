import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


def generate_prophecies(total_num=3, num_sentences=4):
    prophecies = []

    for i in range(total_num):
        forecast = ""
        for j in range(num_sentences):
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)

            full_sentence = f"{t.title()} {a} {p}."
            if j != num_sentences - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence

        prophecies.append(forecast)

    return prophecies


def generate_about():
    uls = []
    times_html_string = "<ol><li>Времена дня</li><ul>"
    advices_html_string = "<li>Глаголы</li><ul>"
    promises_html_string = "<li>События</li><ul>"

    for time in times:
        times_html_string += f"<li>{time}</li>"
    times_html_string += "</ul>"
    uls.append(times_html_string)

    for advice in advices:
        advices_html_string += f"<li>{advice}</li>"
    advices_html_string += "</ul>"
    uls.append(advices_html_string)

    for promise in promises:
        promises_html_string += f"<li>{promise}</li>"
    promises_html_string += "</ul></ol>"
    uls.append(promises_html_string)

    return uls
