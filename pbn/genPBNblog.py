import webbrowser

# Open the HTML template file
with open('seo_structure.html', 'r', encoding="UTF-8") as file:
    html = file.read()

# Open the keywords file
with open('setting.txt', 'r', encoding="UTF-8") as file:
    settings = file.readlines()

# Replace placeholders with keywords
for setting in settings:
    # Split the line by the = character
    keyword_parts = setting.strip().split("=")
    # Get the value of the keyword
    
    keyword_value = keyword_parts[1]
    
    print( keyword_value )
    
    html = html.replace("{Intro}", "5555555")
    html = html.replace("{Topic1}", "This is Topic1 Replacement.")
    html = html.replace("{Web}", keyword_value)
    html = html.replace("{Name}", keyword_value)
    html = html.replace("{Image_url}", keyword_value)
    html = html.replace("{Date}", keyword_value)
    html = html.replace("{Tag}", keyword_value)
    html = html.replace("{Keyword1}", keyword_value)
    html = html.replace("{Keyword2}", keyword_value)
    html = html.replace("{Keyword3}", keyword_value)

# Write the modified HTML to a new file
with open('output.html', 'w') as file:
    file.write(html)

# Open the HTML output in a web browser
webbrowser.open('output.html')
