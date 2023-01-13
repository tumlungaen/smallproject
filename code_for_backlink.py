import random
import webbrowser
import codecs
import html

def main():
    with open("keyword.txt", "r") as file:
        lines = file.readlines()
    with open("comment.txt", "r") as file:
        lines_comment = file.readlines()
    with open("link.txt", "r") as file:
        link = file.readlines()
    unique_lines = random.sample(lines, 6)
    unique_lines_comment = random.sample(lines_comment, 1)
    random.shuffle(unique_lines)
    link = link[0]
    anchor_link1 = f'<a href="{link}" keyword="{unique_lines[0].strip()}" rel="nofollow ugc">{unique_lines[0]}</a> '
    anchor_link2 = f'<a href="{link}" keyword="{unique_lines[1].strip()}" rel="nofollow ugc">{unique_lines[1]}</a> '
    anchor_link3 = f'<a href="{link}" keyword="{unique_lines[2].strip()}" rel="nofollow ugc">{unique_lines[2]}</a> '
    anchor_link4 = f'<a href="{link}" keyword="{unique_lines[3].strip()}" rel="nofollow ugc">{unique_lines[3]}</a> '
    anchor_link5 = f'<a href="{link}" keyword="{unique_lines[4].strip()}" rel="nofollow ugc">{unique_lines[4]}</a> '
    anchor_link6 = f'<a href="{link}" keyword="{unique_lines[5].strip()}" rel="nofollow ugc">{unique_lines[5]}</a> '
    bbcode1 = f'[url={link}]{unique_lines[0]}[/url] '
    bbcode2 = f'[url={link}]{unique_lines[1]}[/url] '
    bbcode3 = f'[url={link}]{unique_lines[2]}[/url] '
    bbcode4 = f'[url={link}]{unique_lines[3]}[/url] '
    bbcode5 = f'[url={link}]{unique_lines[4]}[/url] '
    bbcode6 = f'[url={link}]{unique_lines[5]}[/url] '
    with open("output.html", "w") as file:
        file.write("<!DOCTYPE html><html><head><title>Code For Backlink</title></head><body>")
        file.write( "<h1>1. ลิงค์แบบ Anchor link</h1>" )
        file.write( f'{unique_lines_comment[0]}' + " ")
        file.write(anchor_link1 + "<br />")
        file.write(anchor_link2 + "<br />")
        file.write(anchor_link3 + "<br />")
        file.write(anchor_link4 + "<br />")
        file.write(anchor_link5 + "<br />")
        file.write(anchor_link6 + "<br />")
        file.write( "<h1>2. ลิงค์แบบ HTML</h1>" )
        file.write(f'{unique_lines_comment[0]}' + " ")
        file.write(html.escape( anchor_link1 ) + "<br />")
        file.write(html.escape( anchor_link2 ) + "<br />")
        file.write(html.escape( anchor_link3 ) + "<br />")
        file.write(html.escape( anchor_link4 ) + "<br />")
        file.write(html.escape( anchor_link5 ) + "<br />")
        file.write(html.escape( anchor_link6 ) + "<br />")
        file.write( "<h1>3. ลิงค์แบบ BB Code</h1>" )
        file.write(f'{unique_lines_comment[0]}' + " ")
        file.write(bbcode1 + "<br />")
        file.write(bbcode2 + "<br />")
        file.write(bbcode3 + "<br />")
        file.write(bbcode4 + "<br />")
        file.write(bbcode5 + "<br />")
        file.write(bbcode6 + "<br />")
        file.write("</body></html>")
if __name__ == "__main__":
    main()
    webbrowser.open("output.html")
