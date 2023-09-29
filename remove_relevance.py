import os
from bs4 import BeautifulSoup

html_directory = "reports/"

for file_name in os.listdir(html_directory):
    if file_name.endswith(".html"):
        file_path = os.path.join(html_directory, file_name)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

            element = soup.find_all('i', class_='fa fa-star')
            for e in element:
                parent = e.find_parent()
                parent.decompose()

            element = soup.find_all('i', class_='fa fa-tag')
            for e in element:
                parent = e.find_parent()
                parent.decompose()

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))

print("elements removed from all HTML files in the directory.")
