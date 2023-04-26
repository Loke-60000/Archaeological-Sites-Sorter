import re
from openpyxl import Workbook

class Site:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.commune = self.extract_field("Commune")
        self.numero_insee = self.extract_field("Numéro INSEE")
        self.nom_du_site = self.extract_field("Nom du site")
        self.numero_du_site = self.extract_field("Numéro du site")
        self.coordonnees = self.extract_field("Coordonnées")
        self.circonstance_decouverte = self.extract_field("Circonstance de la découverte")
        self.environnement_relation = self.extract_field("Environnement\\\\relation")
        self.nombre_tombe = self.extract_field("Nombre de tombe")
        self.typologie = self.extract_field("Typologie")
        self.chronologie = self.extract_field("Chronologie")
        self.notices = self.extract_field("Notices")

    def extract_field(self, field_name):
        field_pattern = re.compile(f"{field_name} : (.+)")
        match = field_pattern.search(self.raw_data)
        if match:
            return match.group(1)
        return "non renseigné"

# Read raw_text from data.txt with utf-8 encoding
with open("data.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Split the raw_text into lines
lines = raw_text.strip().split("\n")

# Process the lines to create raw_sites
raw_sites = []
current_site = []
for line in lines:
    if line.strip() == "":
        if current_site:
            raw_sites.append("\n".join(current_site))
            current_site = []
    else:
        current_site.append(line)

if current_site:
    raw_sites.append("\n".join(current_site))

# Create Site objects
sites = [Site(raw_site) for raw_site in raw_sites]

# Sort sites based on the Commune name and Numéro INSEE
sorted_sites = sorted(sites, key=lambda x: (x.commune or "", x.numero_insee or ""))

# Create an Excel file
wb = Workbook()
ws = wb.active

# Header row
ws.append([
    "Commune", "Numéro INSEE", "Nom du site", "Numéro du site", "Coordonnées",
    "Circonstance de la découverte", "Environnement\\relation", "Nombre de tombe",
    "Typologie", "Chronologie", "Notices"
])

# Append data to the Excel sheet
for site in sorted_sites:
    ws.append([
        site.commune, site.numero_insee, site.nom_du_site, site.numero_du_site, site.coordonnees,
        site.circonstance_decouverte, site.environnement_relation, site.nombre_tombe,
        site.typologie, site.chronologie, site.notices
    ])

# Adjust column widths
for col in ws.columns:
    max_length = 0
    column = col[0].column_letter  # Get the column letter
    for cell in col:
        if len(str(cell.value)) > max_length:
            max_length = len(str(cell.value))
    adjusted_width = (max_length + 2) * 1.2
    ws.column_dimensions
    adjusted_width = (max_length + 2) * 1.2
    ws.column_dimensions[column].width = adjusted_width

# Save to Excel file
wb.save("sorted_data.xlsx")
