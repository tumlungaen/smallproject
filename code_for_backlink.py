import random
import webbrowser

#TEST

def main():
    
    # Open the file and read all lines
    with open("file.txt", "r") as file:
        lines = file.readlines()

    # Select a random line from the file
    anchor_text = random.choice(lines)
    keyword = anchor_text.strip()

    # Use the random line as the anchor text and keyword
    link = "https://www.google.com"
    anchor_link1 = f'<a href="{link}" keyword="{keyword}">{anchor_text}</a><br />'
    anchor_link2 = '<a href="{link}" keyword="{keyword}">{anchor_text}</a><br />'

    # Write the anchor link to an HTML file
    with open("output.html", "w") as file:
        file.write(anchor_link1)
        file.write(anchor_link2)

if __name__ == "__main__":
    main()
    webbrowser.open("output.html")
