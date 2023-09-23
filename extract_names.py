import os
from bs4 import BeautifulSoup

report_dir = "reports"
dir = os.listdir(report_dir)

for file in dir:
    file_path = os.path.join(report_dir, file)
    if not file.lower().endswith(".html"):
        continue
    with open(file_path, "r") as f:
        soup = BeautifulSoup(f, "html.parser")
        out = []

        for i in range(
            1,
            len(soup.find_all(id=lambda x: x and x.startswith("candidateheader"))) + 1,
        ):
            candidate_header = soup.find(id=f"candidateheader{i}")
            if candidate_header:
                h5 = candidate_header.find("h5")
                if h5:
                    text = h5.get_text(strip=True)
                    if text:
                        out.append(text[:50])

        output_file_path = os.path.join(report_dir, file[:-4] + "txt")
        with open(output_file_path, "w") as ff:
            for x in out:
                ff.write(x)
                ff.write("\n")
