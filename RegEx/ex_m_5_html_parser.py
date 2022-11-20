import re

text = input()
title_pattern = r"<title>([^<>]*)<\/title>"
body_pattern = r"<body>.*<\/body>"
content_pattern = r">([^><]*)<"

title = "".join(re.findall(title_pattern, text))
print(f"Title: {title}")
body = "".join(re.findall(body_pattern, text))
content = "".join(re.findall(content_pattern, body))
content = content.replace('\\n', '')
print(f'Content: {content}')