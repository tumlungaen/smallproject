import random
import webbrowser
import codecs
import html

def main():
    
    # Open the file and read all lines
    with open("keyword.txt", "r") as file:
        lines = file.readlines()
    
    with open("comment.txt", "r") as file:
        lines_comment = file.readlines()
    
    with open("link.txt", "r") as file:
        link = file.readlines()
        
    # Select a random set of unique lines from the file
    unique_lines = random.sample(lines, 3)
    unique_lines_comment = random.sample(lines_comment, 1)
    
    # Shuffle the unique lines
    random.shuffle(unique_lines)

    # Use the random line as the anchor text and keyword
    link = link[0]
    anchor_link1 = f'<a href="{link}" keyword="{unique_lines[0].strip()}" rel="nofollow ugc">{unique_lines[0]}</a> '
    anchor_link2 = f'<a href="{link}" keyword="{unique_lines[1].strip()}" rel="nofollow ugc">{unique_lines[1]}</a> '
    anchor_link3 = f'<a href="{link}" keyword="{unique_lines[2].strip()}" rel="nofollow ugc">{unique_lines[2]}</a> '
    
    bbcode1 = f'[url={link}]{unique_lines[0]}[/url] '
    bbcode2 = f'[url={link}]{unique_lines[1]}[/url] '
    bbcode3 = f'[url={link}]{unique_lines[2]}[/url] '

    # Write the anchor link to an HTML file
    with open("output.html", "w") as file:
        file.write("<!DOCTYPE html><html><head><title>Code For Backlink</title></head><body>")
        
        file.write( "<h1>1. ลิงค์แบบ Anchor link</h1>" )
        
        file.write( f'{unique_lines_comment[0]}' + " ")
        file.write(anchor_link1 + "<br />")
        file.write(anchor_link2 + "<br />")
        file.write(anchor_link3 + "<br />")
        
        
        file.write( "<h1>2. ลิงค์แบบ HTML</h1>" )
        file.write(f'{unique_lines_comment[0]}' + " ")
        file.write(html.escape( anchor_link1 ) + "<br />")
        file.write(html.escape( anchor_link2 ) + "<br />")
        file.write(html.escape( anchor_link3 ) + "<br />")
        
        file.write( "<h1>3. ลิงค์แบบ BB Code</h1>" )
        file.write(f'{unique_lines_comment[0]}' + " ")
        file.write(bbcode1 + "<br />")
        file.write(bbcode2 + "<br />")
        file.write(bbcode3 + "<br />")

        file.write("</body></html>")
        
if __name__ == "__main__":
    main()
    webbrowser.open("output.html")
