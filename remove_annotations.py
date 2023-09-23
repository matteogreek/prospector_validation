import os
from bs4 import BeautifulSoup

html_directory = "reports/relevance_sorted/norules/"

for file_name in os.listdir(html_directory):
    if file_name.endswith(".html"):
        file_path = os.path.join(html_directory, file_name)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

        for icon in soup.find_all("i", class_="fas fa-bullhorn"):
            icon.decompose()

        for span in soup.find_all("span", class_="badge rounded-pill bg-primary", style="font-family: monospace;"):
            span.decompose()
    
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))

print("elements removed from all HTML files in the directory.")
