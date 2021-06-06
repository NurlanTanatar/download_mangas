import os

def check_for_missing_files(file_name):
    REPORTS_FOLDER = "zips"

    files = os.listdir(REPORTS_FOLDER)

    urls = []
    missing = []
    with open(f'{file_name}.txt', 'r', encoding='utf-8') as links:
        for line in links:
            line = line.strip()
            urls.append(line)

    for url in urls:
        firstpos=url.rfind("/")
        lastpos=len(url)
        if url[firstpos+1:lastpos] in files:
            pass
        else:
            print(f"url: {url}")
    
    with open('missing.txt', 'w', encoding='utf-8') as file:
        for line in range(len(missing)):
            file.write(f"{missing[line]}\n")