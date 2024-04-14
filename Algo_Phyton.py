# Algorithme
""" 
Algorithme afficher_table_et_formes_canoniques(logique):
    variables <- extraire_variables(logique)
    nombre_variables <- longueur(variables)
    table_de_verite <- generer_table_de_verite(nombre_variables)

    afficher_entete_table_de_verite(variables, logique)

    Pour chaque ligne dans table_de_verite:
        resultats <- evaluer_fonction_logique(logique, ligne)
        afficher_ligne_table_de_verite(ligne, resultats)

    premiere_forme_canonique <- calculer_premiere_forme_canonique(table_de_verite, logique)
    deuxieme_forme_canonique <- calculer_deuxieme_forme_canonique(table_de_verite, logique)

    afficher("Première forme canonique :", premiere_forme_canonique)
    afficher("Deuxième forme canonique :", deuxieme_forme_canonique)

    Fin Algorithme
"""

from itertools import product

def extraire_variables(logique):
    return sorted(set([c for c in logique if c.isalpha()]))

def generer_table_de_verite_ordre(nb_variables):
    table = []

    def generate_helper(current_values):
        if len(current_values) == nb_variables:
            table.append(tuple(current_values))
        else:
            generate_helper(current_values + [False])
            generate_helper(current_values + [True])

    generate_helper([])
    return table

def evaluer_fonction_logique(logique, ligne):
    valeurs = dict(zip(variables, ligne))
    return eval(logique, valeurs)

def calculer_premiere_forme_canonique(table_de_verite, logique):
    premiere_forme = ""
    for i, row in enumerate(table_de_verite):
        if evaluer_fonction_logique(logique, row):
            minterm = " AND ".join([f"({variables[j]} OR NOT {variables[j]})" if val else f"({variables[j]} OR NOT {variables[j]})" for j, val in enumerate(row)])
            premiere_forme += f"({minterm}){' OR ' if i < len(table_de_verite) - 1 else ''}"
    return premiere_forme

def calculer_deuxieme_forme_canonique(table_de_verite, logique):
    deuxieme_forme = ""
    for i, row in enumerate(table_de_verite):
        if not evaluer_fonction_logique(logique, row):
            maxterm = " AND ".join([f"({variables[j]} if val else f'NOT {variables[j]}')" for j, val in enumerate(row)])
            deuxieme_forme += f"({maxterm}){' OR ' if i < len(table_de_verite) - 1 else ''}"
    return deuxieme_forme

def afficher_entete_table_de_verite(variables, logique):
    entete = ' | '.join(variables + [logique])
    print(entete)
    print('-' * len(entete))

def afficher_ligne_table_de_verite(ligne, resultats):
    ligne_str = ' | '.join([str(int(val)) for val in ligne] + [str(int(resultats))])
    print(ligne_str)

# Définir la fonction logique
logique = "(A and not B) or (not A and not B)"

# Extraire les variables de la fonction logique
variables = extraire_variables(logique)

# Générer la table de vérité
table_de_verite = generer_table_de_verite_ordre(len(variables))

# Afficher la table de vérité
afficher_entete_table_de_verite(variables, logique)
for ligne in table_de_verite:
    resultats = evaluer_fonction_logique(logique, ligne)
    afficher_ligne_table_de_verite(ligne, resultats)

# Calculer et afficher les formes canoniques
premiere_forme = calculer_premiere_forme_canonique(table_de_verite, logique)
deuxieme_forme = calculer_deuxieme_forme_canonique(table_de_verite, logique)
print("Première forme canonique :", premiere_forme)
print("Deuxième forme canonique :", deuxieme_forme)

