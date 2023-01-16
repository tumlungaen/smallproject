import webbrowser
import random
keyword_counter = 0

def insert_keywords_backup(article, keywords_dict, probability):
    words = article.split()
    rand_num = random.random()
    if rand_num < probability: # Insert keyword
        rand_keyword = random.choice([keywords_dict.get("Keyword1"),keywords_dict.get("Keyword2"),keywords_dict.get("Keyword3")])
        rand_index = random.randint(0, len(words))
        words.insert(rand_index,rand_keyword)
    else:  # Insert empty string
        rand_index = random.randint(0, len(words))
        words.insert(rand_index,'')
    return " ".join(words)

def insert_keywords(article, keywords_dict, probability):
    words = article.split()
    rand_num = random.random()
    if rand_num < probability: # Insert keyword
        rand_keyword = random.choice([keywords_dict.get("Keyword1"),keywords_dict.get("Keyword2"),keywords_dict.get("Keyword3")])
        rand_index = random.randint(0, len(words))
        rand_web = random.choice([keywords_dict.get("Web1"), keywords_dict.get("Web2")])
        anchor_text = f'<a href="{rand_web}" keyword="{rand_keyword}" rel="follow">{rand_keyword}</a>'
        words.insert(rand_index,anchor_text)
    else:  # Insert empty string
        rand_index = random.randint(0, len(words))
        words.insert(rand_index,'')
    return " ".join(words)
    
# Open the HTML template file
with open('seo_structure_full.html', 'r') as file:
    html = file.read()

# Open the keywords file
with open('setting.txt', 'r') as file:
    settings = file.readlines()
    settings_dict = {}
    for setting in settings:
        # Split the line by the = character
        keyword_parts = setting.strip().split("=")
        # Get the key and value of the keyword
        keyword_key = keyword_parts[0]
        keyword_value = keyword_parts[1]
        settings_dict[keyword_key] = keyword_value

# Open the topics file and create a list
with open('topic.txt', 'r') as file:
    topics = file.readlines()
    subtopics = file.readlines()

# Open the articles file and create a list
with open('article.txt', 'r') as file:
    articles = file.readlines()

# Replace placeholders with keywords
html = html.replace("{Intro}", settings_dict.get("Intro"))
html = html.replace("{Web1}", settings_dict.get("Web1"))
html = html.replace("{Web2}", settings_dict.get("Web2"))
html = html.replace("{Name}", settings_dict.get("Name"))
html = html.replace("{Image_url1}", settings_dict.get("Image_url1"))
html = html.replace("{Image_url2}", settings_dict.get("Image_url2"))
html = html.replace("{Image_url3}", settings_dict.get("Image_url3"))
html = html.replace("{Date}", settings_dict.get("Date"))
html = html.replace("{Tag}", settings_dict.get("Tag"))
html = html.replace("{Keyword1}", settings_dict.get("Keyword1"))
html = html.replace("{Keyword2}", settings_dict.get("Keyword2"))
html = html.replace("{Keyword3}", settings_dict.get("Keyword3"))

# Replace placeholders with topics
html = html.replace("{Topic1}", topics[0].strip())

for i, topic in enumerate(topics[1:]):
    placeholder = f"{{Topic2-{i+1}}}"
    html = html.replace(placeholder, topic.strip())

#for i, subtopic in enumerate(subtopics):
for i, subtopic in enumerate(topics[5:]):
    placeholder = f"{{Topic3-{i+1}}}"
    html = html.replace(placeholder, subtopic.strip())

for i, article in enumerate(articles):
    
    placeholder = f"{{article{i+1}}}"
    html = html.replace(placeholder, insert_keywords( article.strip(), settings_dict, 0.10 ) )
    

# Write the modified HTML to a new file
with open('output.html', 'w') as file:
    file.write(html)

# Open the HTML output in a web browser
webbrowser.open('output.html')
