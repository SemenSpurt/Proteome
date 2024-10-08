import os

os.makedirs("Plots", exist_ok=True)
os.makedirs("Data", exist_ok=True)

runs = {
    "Sputum" : "/home/selezov_su/Proteomics/Viruses/SearchPeptidesInSputum/combined/txt/",
    "Smears" : "/home/selezov_su/Proteomics/Viruses/Smears/combined/txt/",
    "DBS"    : "/home/selezov_su/Proteomics/DryBloodSample/combined/txt/",
    "smear"  : "/home/selezov_su/MsData/NewRunSmears/combined/txt/",
    "sputum" : "/home/selezov_su/MsData/NewRunSputum/combined/txt/"
}
name = "smear"
data_path = runs[name]

def parse_proteins_in_file(filepath):
    with open(filepath, "r") as file:
        return file.read().splitlines()