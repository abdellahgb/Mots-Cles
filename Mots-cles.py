import os
from PyPDF2 import PdfReader

class Couleurs:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def recherche_dans_pdf(chemin_fichier, mot_cle):
    try:
        lecteur = PdfReader(chemin_fichier)
        for page in lecteur.pages:
            if mot_cle.lower() in page.extract_text().lower():
                return True
    except Exception as e:
        print(f"{Couleurs.FAIL}Erreur lors de la lecture de {chemin_fichier}: {e}{Couleurs.ENDC}")
    return False

def recherche_dans_texte(chemin_fichier, mot_cle):
    try:
        with open(chemin_fichier, 'r', encoding='utf-8', errors='ignore') as fichier:
            contenu = fichier.read()
            return mot_cle.lower() in contenu.lower()
    except Exception as e:
        print(f"{Couleurs.FAIL}Erreur lors de la lecture de {chemin_fichier}: {e}{Couleurs.ENDC}")
    return False

def recherche_cv(mot_cle, dossier_path):
    chemin_fichier_resultats = os.path.join(dossier_path, f"{mot_cle}.txt")
    
    compteur_resultats = 0
    compteur_pdf = 0
    compteur_txt = 0
    compteur_autres = 0
    total_fichiers = 0

    with open(chemin_fichier_resultats, 'w', encoding='utf-8') as fichier_resultats:
        if not os.path.exists(dossier_path):
            print(f"{Couleurs.FAIL}Le dossier '{dossier_path}' n'existe pas.{Couleurs.ENDC}")
            return

        print(f"{Couleurs.HEADER}*** Début de la recherche ***{Couleurs.ENDC}\n")
        
        for nom_fichier in os.listdir(dossier_path):
            chemin_fichier = os.path.join(dossier_path, nom_fichier)
            total_fichiers += 1

            if nom_fichier.endswith('.pdf'):
                compteur_pdf += 1
                if recherche_dans_pdf(chemin_fichier, mot_cle):
                    fichier_resultats.write(f"{chemin_fichier}\n")
                    fichier_resultats.write("_" * 64 + "\n")
                    compteur_resultats += 1
                    print(f"{Couleurs.OKGREEN}Mot-clé trouvé dans PDF: {chemin_fichier}{Couleurs.ENDC}")
            
            elif nom_fichier.endswith('.txt'):
                compteur_txt += 1
                if recherche_dans_texte(chemin_fichier, mot_cle):
                    fichier_resultats.write(f"{chemin_fichier}\n")
                    fichier_resultats.write("_" * 64 + "\n")
                    compteur_resultats += 1
                    print(f"{Couleurs.OKBLUE}Mot-clé trouvé dans TXT: {chemin_fichier}{Couleurs.ENDC}")
            
            else:
                compteur_autres += 1
                if recherche_dans_texte(chemin_fichier, mot_cle):
                    fichier_resultats.write(f"{chemin_fichier}\n")
                    fichier_resultats.write("_" * 64 + "\n")
                    compteur_resultats += 1
                    print(f"{Couleurs.OKCYAN}Mot-clé trouvé dans Autre fichier: {chemin_fichier}{Couleurs.ENDC}")

        fichier_resultats.write("\n" + "_" * 64 + "\n")
        fichier_resultats.write(f"Nombre de résultats trouvés: {compteur_resultats}\n")
        fichier_resultats.write(f"Nombre total de fichiers analysés: {total_fichiers}\n")
        fichier_resultats.write(f"Nombre de fichiers PDF: {compteur_pdf}\n")
        fichier_resultats.write(f"Nombre de fichiers TXT: {compteur_txt}\n")
        fichier_resultats.write(f"Nombre de fichiers Autres: {compteur_autres}\n")

    print(f"\n{Couleurs.HEADER}*** Résumé des résultats ***{Couleurs.ENDC}")
    print(f"{Couleurs.BOLD}Nombre de résultats trouvés: {Couleurs.OKCYAN}{compteur_resultats}{Couleurs.ENDC}")
    print(f"{Couleurs.BOLD}Nombre total de fichiers analysés: {Couleurs.OKCYAN}{total_fichiers}{Couleurs.ENDC}")
    print(f"{Couleurs.BOLD}Nombre de fichiers PDF: {Couleurs.OKCYAN}{compteur_pdf}{Couleurs.ENDC}")
    print(f"{Couleurs.BOLD}Nombre de fichiers TXT: {Couleurs.OKCYAN}{compteur_txt}{Couleurs.ENDC}")
    print(f"{Couleurs.BOLD}Nombre de fichiers Autres: {Couleurs.OKCYAN}{compteur_autres}{Couleurs.ENDC}")
    print(f"{Couleurs.OKGREEN}Résultats sauvegardés dans le fichier: {chemin_fichier_resultats}{Couleurs.ENDC}")

    #my pf
    print(f"{Couleurs.OKBLUE}\nPour toute question ou collaboration, n'hésitez pas à me contacter sur LinkedIn : https://www.linkedin.com/in/abdellah-abbassi-3399b02a7{Couleurs.ENDC}")

dossier_path = input(f"{Couleurs.BOLD}Entrez le chemin du dossier contenant les CV: {Couleurs.ENDC}")
mot_cle = input(f"{Couleurs.BOLD}Entrez le mot-clé de recherche: {Couleurs.ENDC}")

recherche_cv(mot_cle, dossier_path)
