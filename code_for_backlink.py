import random
import webbrowser
import codecs
 
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
    anchor_link1 = f'<a href="{link}" keyword="{keyword1}">{anchor_text1}</a><br />'
    anchor_link2 = f'<a href="{link}" keyword="{keyword2}">{anchor_text2}</a><br />'
    anchor_link3 = f'<a href="{link}" keyword="{keyword3}">{anchor_text3}</a><br />'

    # Write the anchor link to an HTML file
    with open("output.html", "w") as file:
        file.write("<!DOCTYPE html><html><head><title>Code For Backlink</title></head><body>")
        file.write(anchor_link1)
        file.write("<pre><plaintext>Test")
        file.write(anchor_link2)
        file.write("</plaintext></pre>")
        file.write(anchor_link3)
        file.write("</body></html>")

if __name__ == "__main__":
    main()
    webbrowser.open("output.html")
