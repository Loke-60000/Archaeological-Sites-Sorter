import re
from openpyxl import Workbook

class Site:
    def __init__(self, name, site_number, bibliography):
        self.name = name
        self.site_number = site_number
        self.bibliography = bibliography

def extract_sites_from_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        site_blocks = data.split("\n\n")

    sites = []

    for block in site_blocks:
        name = re.search(r"Nom du site : (.+)", block)
        site_number = re.search(r"Numéro du site : (.+)", block)
        bibliography = re.findall(r"Bibliographie :(.+)", block)

        if name and site_number and bibliography:
            bibliography = "\n".join([f"{index + 1}. {ref.strip()}" for index, ref in enumerate(bibliography)])
            sites.append(Site(name.group(1), site_number.group(1), bibliography))

    return sites

def write_sites_to_excel(sites, output_file):
    wb = Workbook()
    ws = wb.active
    ws.append(["Nom du site", "Numéro du site", "Bibliographie"])
    
    # Set the width of the "Bibliographie" column
    ws.column_dimensions['C'].width = 500

    for site in sites:
        ws.append([site.name, site.site_number, site.bibliography])

    wb.save(output_file)

def main():
    data_file = "data.txt"
    output_file = "bibliography_sorted_data.xlsx"
    
    sites = extract_sites_from_data(data_file)
    write_sites_to_excel(sites, output_file)

if __name__ == "__main__":
    main()

