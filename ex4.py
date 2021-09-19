import re

def mot_correspondant (mot:str,motif:str)->bool:
    """[summary] verifie si un motif et present dans mot

    Args:
        mot (str):mot fournit
        motif (str): motif peux contenir des jokers (.)

    Returns:
        bool: True si motif present False sinon
    """
    correspond = False
    if(re.match(motif,mot)):
        correspond = True
    return correspond

def presente(lettre:str,mot:str)->list:
    """fonction verifiant si lettre et present dans mot

    Args:
        lettre (str): lettre rechercher
        mot (str): mot

    Returns:
        int: indice de la lettre
    """
    index_return = []
    for index in range(len(mot)):
        if lettre == mot[index]:
            index_return.append(index)
    return index_return


def mots_Nlettres(liste_mots:list,nbr_lettres:int) -> list: # Malo
    """Retourne les mots parmis la liste en paramètre contenant le nombre de lettre passé en paramètre

    Args:
        liste_mots (list): Liste de mots dans laquelle effectuer la recherche
        nbr_lettres (int): Nombre de lettre

    Returns:
        list: Liste comprenant le nombre de lettres spécifiées
    """
    liste_de_retour = []
    for mot in liste_mots:
        if len(mot) == nbr_lettres:
            liste_de_retour.append(mot)
    return liste_de_retour

def dictionnaire(nom_fichier:str) -> list[str]:
    """Retourne la liste des mots contenu dans un fichier texte dont le nom est passé en paramètre

    Args:
        nom_fichier (str): Nom du fichier a lire

    Returns:
        list[str]: Liste des mots contenus dans le fichier
    """
    with open(nom_fichier, "r",encoding="UTF-8") as fichier:
        dictionnaire = fichier.read().lower()
    fichier.close()
    return dictionnaire.split("\n")

def mot_optimaux(dico:list,lettres:str)->list:
    """

    Args:
        dico (list):mots disponible en fonction de lettre
        lettres (str): permet de restreidre le nombre de mot

    Returns:
        list: mot disponible
    """
    regex = "^"+lettres+"{1}[a-z]*"
    mot_apres_regex = []
    for element in dico:
        if re.match(regex,element):
            mot_apres_regex.append(element)
    longueur_element = len(mot_apres_regex[0])
    if(m)
    for index in range(len(mot_apres_regex)):
        if(longueur_element<len(mot_apres_regex[index])):
            longueur_element = len(mot_apres_regex[index])

    liste_finale = mots_Nlettres(mot_apres_regex,longueur_element)
    return liste_finale
    
mot_optimaux(dictionnaire("dico.txt"),"para")
    
    



