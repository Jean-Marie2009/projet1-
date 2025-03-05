import pandas as pd

# Fonction pour valider une note
def valider_note(message):
    while True:
        note = input(message)
        if note.replace(".", "", 1).isdigit():  # Vérifie si c'est un nombre valide
            return float(note)
        print("Erreur : Veuillez entrer un nombre valide.")

# Fonction pour calculer la moyenne selon la méthode spécifiée
def calculer_moyenne(interro1, interro2, devoir1, devoir2, coefficient):
    moyenne_interros = (interro1 + interro2) / 2
    moyenne_devoirs = (devoir1 + devoir2) / 2
    moyenne_matiere = (moyenne_interros + moyenne_devoirs) / 3
    return moyenne_matiere * coefficient

# Saisie du nombre de matières
nombre_matieres = int(input("Entrez le nombre de matières : "))

# Saisie des coefficients pour chaque matière
coefficients = []
for i in range(nombre_matieres):
    coeff = valider_note(f"Entrez le coefficient pour la matière {i + 1} : ")
    coefficients.append(coeff)

# Saisie des notes pour chaque élève
eleves = []
while True:
    nom = input("\nEntrez le nom de l'élève (ou 'fin' pour terminer) : ")
    if nom.lower() == 'fin':
        break

    notes_eleve = []
    for i in range(nombre_matieres):
        print(f"\nMatière {i + 1} :")
        interro1 = valider_note("  Note d'interrogation 1 : ")
        interro2 = valider_note("  Note d'interrogation 2 : ")
        devoir1 = valider_note("  Note de devoir 1 : ")
        devoir2 = valider_note("  Note de devoir 2 : ")

        # Calcul de la moyenne pondérée pour la matière
        moyenne_ponderee = calculer_moyenne(interro1, interro2, devoir1, devoir2, coefficients[i])
        notes_eleve.append(moyenne_ponderee)

    # Ajout de l'élève et de ses notes pondérées
    eleves.append({"Élève": nom, **{f"Matière {i + 1}": note for i, note in enumerate(notes_eleve)}})

# Création du DataFrame
df = pd.DataFrame(eleves)

# Calcul de la moyenne générale de chaque élève
df["Moyenne Générale"] = df.apply(lambda row: sum(
    [row[f"Matière {i + 1}"] for i in range(nombre_matieres)]
) / sum(coefficients), axis=1)

# Calcul de la moyenne de la classe
moyenne_classe = df["Moyenne Générale"].mean()

# Affichage des résultats
print("\nTableau des notes et des moyennes :")
print(df)
print(f"\nMoyenne de la classe : {moyenne_classe:.2f}")