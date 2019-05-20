from horoscope import generate_prophecies
from datetime import datetime as dt


def generate_page(head, body, link):
    page = f"<html>{head}{body}{link}</html>"
    return page


def generate_head(title):
    head = f"""<head>
    <meta charset="utf-8">
    <title>{title}</title>
    </head>
    """
    return head


def generate_body(header, paragraphs):
    body = f"<h1>{header}</h1><hr>"
    for p in paragraphs:
        body = body + f"<p><li>{p}</li></p>"
    return f"<body>{body}</body><hr>"


def generate_link(link):
    link = f"<p><a href={link}>«О реализации»</a></p>"
    return f"<p><a href={link}</a></p>"


def save_page(title, header, paragraphs, link, output="index.html"):
    fp = open(output, "w")
    page = generate_page(
        head=generate_head(title),
        body=generate_body(header=header, paragraphs=paragraphs),
        link=generate_link(link=link))
    print(page, file=fp)
    fp.close()


#####################

today = dt.now().date()

save_page(
    title="Гороскоп на сегодня",
    header="Что день " + str(today) + " готовит",
    paragraphs=generate_prophecies(),
    link="about.html"
)
