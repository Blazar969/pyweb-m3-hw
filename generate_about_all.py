list_paragraphs = {"Времена дня": ["утром", "вечером", "после обеда"],
                   "Глаголы": ["остерегайтесь", "ожидайте"],
                   "Ожидание": ["ожидайте", "предостерегайтесь", "будьте открыты для"]}


def generate_page(head, body):
    page = f"""<html>
    {head}
    {body}
    </html>"""
    return page


def generate_head(title):
    head = f"""<head>
    <meta charset='utf-8'>
    <title>{title}</title>
    </head>
    """
    return head


def generate_html_list(li_elements):
    html_list = ""
    for ol_elem in li_elements:
        html_list += f'<li>{ol_elem}</li><ul>'
        for ul_elem in li_elements[ol_elem]:
            html_list += f"<li>{ul_elem}</li>"
        html_list += '</ul>'
    return f"<ol>{html_list}</ol>"


def generate_link(link_text, link_page):
    return f'<a href = "{link_page}">{link_text}</a>'


def generate_icon(img_name, img_width, img_height):
    return f'<img src = "{img_name}" width="{img_width}" height="{img_height}">'


def generate_body(header, list_elements):
    html_list = generate_html_list(list_elements)
    icon = generate_icon("zodiac_pic.jpg", img_width=100, img_height=100)

    html_page_content = f'''{icon}
                        {html_list}
                        {generate_link("На главную", "index.html")}'''

    body = f"""<h1>{header}</h1>
    {html_page_content} """

    return f"<body>{body}</body>"


def save_page(title, header, list_elements, output="about.html"):

    fp = open(output, "w")

    page = generate_page(head=generate_head(title),
                         body=generate_body(header, list_elements))
    print(page, file=fp)
    fp.close()


save_page(title="About",
          header="О чем все это",
          list_elements=list_paragraphs)
