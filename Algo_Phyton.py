# Algorithme
""" Algorithme afficher_table_et_formes_canoniques(logique):
    variables <- extraire_variables(logique)
    nombre_variables <- longueur(variables)
    table_de_verite <- generer_table_de_verite(nombre_variables)

    afficher_entete_table_de_verite(variable¬s, logique)

    Pour chaque ligne dans table_de_verite:
    resultats <- evaluer_fonction_logique(logique, ligne)
    afficher_ligne_table¬_de_verite(ligne, resultats)

    premiere_forme_canonique <- calculer_premiere_forme_canonique(table_de_verite, logique)
    deuxieme_forme_canonique <- calculer_deuxieme_forme_canonique(table_de_verite, logique)

    afficher("Première forme canonique :", premiere_forme_canonique)
    afficher("Deuxième forme canonique :", deuxieme_forme_canonique)

    Fin Algorithme
"""


from itertools import product

def extraire_variables(logique):
 return sorted(set([c for c in logique if c.isalpha()]))

def generer_table_de_verite(nb_variables):
 return list(product([False, True], repeat=nb_variables))

def evaluer_fonction_logique(logique, ligne):
    valeurs = dict(zip(variables, ligne))
    return eval(logique, valeurs)

def calculer_premiere_forme_canonique(table_de_verite, logique):
    premier_forme = ""
    for i, row in enumerate(table_de_verite):
        if evaluer_fonction_logique(logique, row):
            minterm = " AND ".join([f"({variables[j]} OR NOT {variables[j]})" if val else f"({variables[j]} OR NOT {variables[j]})" for j, val in enumerate(row)])
            premier_forme += f"({minterm}){' OR ' if i < len(table_de_verite) - 1 else ''}"
    return premier_forme

def calculer_deuxieme_forme_canonique(table_de_verite, logique):
    deuxieme_forme = ""
    for i, row in enumerate(table_de_verite):
            if not evaluer_fonction_logique(logique, row):
                maxterm = " OR ".join([f"({variables[j]} AND NOT {variables[j]})" if val else f"({variables[j]} AND NOT {variables[j]})" for j, val in enumerate(row)])
    deuxieme_forme += f"({maxterm}){' AND ' if i < len(table_de_verite) - 1 else ''}"
    return deuxieme_forme

def afficher_entete_table_de_verite(variables, logique):
    entete = ' | '.join(variables + [logique])
    print(entete)
    print('-' * len(entete))

def afficher_ligne_table_de_verite(ligne, resultats):
    ligne_str = ' | '.join([str(int(val)) for val in ligne] + [str(int(resultats))])
    print(ligne_str)

# Définir la fonction logique
logique = "(A and B)or (C and D)"

# Extraire les variables de la fonction logique
variables = extraire_variables(logique)

# Générer la table de vérité
table_de_verite = generer_table_de_verite(len(variables))

# Afficher la table de vérité
afficher_entete_table_de_verite(variables, logique)
for ligne in table_de_verite:
    resultats = evaluer_fonction_logique(logique, ligne)
    afficher_ligne_table_de_verite(ligne, resultats)

# Calculer et afficher les formes canoniques
premiere_forme = calculer_premiere_forme_canonique(table_de_verite, logique)
deuxieme_forme = calculer_deuxieme_forme_canonique(table_de_verite, logique)
print("\nPremière forme canonique :", premiere_forme)
print("\nDeuxième forme canonique :", deuxieme_forme)

