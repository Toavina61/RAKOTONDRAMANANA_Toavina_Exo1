#Algorithme: Définition des fonctions logiques et affichage des tables de vérité
"""Algorithme Afficher_Table_Verite_et_Formes_Canoniques():
    Afficher "A\tB\t¬A\t¬B\tA∧¬B\t¬A∧¬B\tF"
    Afficher "-----------------------------"
    Pour chaque A dans [Faux, Vrai]:
        Pour chaque B dans [Faux, Vrai]:
            not_A <- 1 - A
            not_B <- 1 - B
            term1 <- A ET ¬B
            term2 <- ¬A ET ¬B
            F <- term1 OU term2
            Afficher A, B, not_A, not_B, term1, term2, F

    Afficher "Table de vérité pour la forme canonique conjonctive :"
    Afficher "A\tB\tC\tF"
    Afficher "------------------"
    Pour chaque A dans [Faux, Vrai]:
        Pour chaque B dans [Faux, Vrai]:
            Pour chaque C dans [Faux, Vrai]:
                termes <- [(A OU B OU C), (A OU ¬B OU C), (A OU ¬B OU ¬C), (¬A OU B OU ¬C)]
                resultat <- tous(termes)
                Afficher A, B, C, resultat

    Afficher "Table de vérité pour la forme canonique disjonctive :"
    Afficher "A\tB\tC\tF"
    Afficher "------------------"
    Pour chaque A dans [Faux, Vrai]:
        Pour chaque B dans [Faux, Vrai]:
            Pour chaque C dans [Faux, Vrai]:
                termes <- [(A ET B ET C), (A ET ¬B ET C), (A ET ¬B ET ¬C), (¬A ET B ET ¬C)]
                resultat <- n'importe_quel(termes)
                Afficher A, B, C, resultat
    Fin de l'algorithme
"""

# Premier programme: Définition des fonctions logiques et affichage des tables de vérité
def evaluate_F(A, B):
    not_A = 1 - A
    not_B = 1 - B
    term1 = A and not_B
    term2 = not_A and not_B
    F = term1 or term2
    return not_A, not_B, term1, term2, F

def truth_table_F():
    print("A\tB\t¬A\t¬B\tA∧¬B\t¬A∧¬B\tF")
    print("-----------------------------")
    for A in [0, 1]:
        for B in [0, 1]:
            not_A, not_B, term1, term2, F = evaluate_F(A, B)
            print(f"{A}\t{B}\t{not_A}\t{not_B}\t{term1}\t{term2}\t{F}")

def forme_canonique_disjonctive(A, B, C):
    termes = [
        (A and B and C),
        (A and not B and C),
        (A and not B and not C),
        (not A and B and not C)
    ]
    return any(termes)

def forme_canonique_conjonctive(A, B, C):
    termes = [
        (A or B or C),
        (A or not B or C),
        (A or not B or not C),
        (not A or B or not C)
    ]
    return all(termes)

def table_verite(forme_canonique):
    print("A\tB\tC\tF")
    print("------------------")
    for A in [False, True]:
        for B in [False, True]:
            for C in [False, True]:
                resultat = forme_canonique(A, B, C)
                print(f"{int(A)}\t{int(B)}\t{int(C)}\t{int(resultat)}")

print("Premier programme: Définition des fonctions logiques et affichage des tables de vérité")
truth_table_F()

# Tables de vérité pour les formes canoniques
print("\nTable de vérité pour la forme canonique conjonctive :")
table_verite(forme_canonique_conjonctive)

print("\nTable de vérité pour la forme canonique disjonctive :")
table_verite(forme_canonique_disjonctive)


# Algorithme: Affiche la table de verite et la calcule des deux forme canonique
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


#Deuxieme programe: Affiche la table de verite et la calcule des deux forme canonique

print("Deuxieme programe: Affiche la table de verite et la calcule des deux forme canonique")
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

def afficher_table_et_formes_canoniques(logique):
    variables = extraire_variables(logique)
    table_de_verite = generer_table_de_verite_ordre(len(variables))

    afficher_entete_table_de_verite(variables, logique)
    for ligne in table_de_verite:
        resultats = evaluer_fonction_logique(logique, ligne)
        afficher_ligne_table_de_verite(ligne, resultats)

# Définir la fonction logique
logique = "(A and not B) or (not A and not B)"

# Extraire les variables de la fonction logique
variables = extraire_variables(logique)

# Générer la table de vérité
table_de_verite = generer_table_de_verite_ordre(len(variables))

# Afficher la table de vérité et les formes canoniques
afficher_table_et_formes_canoniques(logique)

# Calculer et afficher les formes canoniques
premiere_forme = calculer_premiere_forme_canonique(table_de_verite, logique)
deuxieme_forme = calculer_deuxieme_forme_canonique(table_de_verite, logique)
print("Première forme canonique :", premiere_forme)
print("Deuxième forme canonique :", deuxieme_forme)
