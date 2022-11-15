title = input()
content = input()
comments = []
while True:
    command = input()
    if command == "end of comments":
        break
    comments.append(command)

print("<h1>")
print(f"\t{title}")
print("</h1>")
print("<article>")
print(f"\t{content}")
print("</article>")

for comment in comments:
    print("<div>")
    print(f"\t{comment}")
    print("</div>")
