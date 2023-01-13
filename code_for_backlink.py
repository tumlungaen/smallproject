import random
import webbrowser
<<<<<<< HEAD
import codecs
import html
 
=======

#TEST

>>>>>>> d6e0275385e215ff27337933bb499c80f394e351
def main():
    
    # Open the file and read all lines
    with open("file.txt", "r") as file:
        lines = file.readlines()

    # Select a random line from the file
    anchor_text1 = random.choice(lines)
    keyword1 = anchor_text1.strip()
    
    anchor_text2 = random.choice(lines)
    keyword2 = anchor_text2.strip()
    
    anchor_text3 = random.choice(lines)
    keyword3 = anchor_text3.strip()

    # Use the random line as the anchor text and keyword
    link = "https://www.google.com"
    anchor_link1 = f'<a href="{link}" keyword="{keyword1}">{anchor_text1}</a> '
    anchor_link2 = f'<a href="{link}" keyword="{keyword2}">{anchor_text2}</a> '
    anchor_link3 = f'<a href="{link}" keyword="{keyword3}">{anchor_text3}</a> '

    # Write the anchor link to an HTML file
    with open("output.html", "w") as file:
        file.write("<!DOCTYPE html><html><head><title>Code For Backlink</title></head><body>")
        file.write(anchor_link1)
        file.write("<pre><code>")
        file.write(html.escape( anchor_link2 ))
        file.write("</code></pre>")
        file.write(anchor_link3)
        file.write("</body></html>")

if __name__ == "__main__":
    main()
    webbrowser.open("output.html")
