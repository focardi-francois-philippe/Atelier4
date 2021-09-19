import re

def full_name(str_arg:str)->str:
    chaine = str_arg.split(" ")
    chaine[0] = chaine[0].upper()
    chaine[1] = chaine[1].capitalize()
    chaine = ' '.join(chaine)
    return chaine

def saisie_full_name()->None:
    """Fonction de saisie
    """
    regex = "^[a-z|A-Z]{2,}[ ]{1}[a-z|A-Z]{2,} *$"
    nom_prenom = input("Saisissez votre nom et votre prenom separer d'un espace: ")
    chaine_with_regex = re.match(regex,nom_prenom)
    if(chaine_with_regex != None):
        full_name(nom_prenom)
    else:
        print("ERREUR DANS L'ECRITURE")

def is_mail(str_arg:str)->tuple:
    """verifie que l'email est sous un bon format

    Args:
        str_arg (str): email

    Returns:
        tuple: (validite,code erreur)
    """
    regex = '[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
    emailValide = (0,0)
    if(re.fullmatch(regex,str_arg)):
        emailValide = (1,-1)
    else:
        if(str_arg.find("@")!=-1):
            chaineCouper = str_arg.split("@")
            if(chaineCouper[1].find(".")!=-1):
                emailValide = (0,1)
            else:
                emailValide = (0,4)
        else:
            emailValide = (0,2)
    return emailValide
def test_is_mail():
    print("TEST DE LA FONCTION is_mail")
    str_variable2test = "bisgambiglia_paul@univ-corse.fr"
    print("PREMIER TEST : {} email valide resultat doit etre  (1,x). RESULTAT = ".format(str_variable2test),is_mail(str_variable2test))
    str_variable2test =  "bisgambiglia_paulOuniv-corse.fr"
    print("DEUXIEME TEST : {} email pas valide  resultat doit etre  (0,2).  RESULTAT = ".format(str_variable2test),is_mail(str_variable2test))
    str_variable2test =  "bisgambiglia_paul@univ-corsePOINTfr"
    print("TROISIEME TEST : {} email valide resultat doit etre  (0,4).  RESULTAT = ".format(str_variable2test),is_mail(str_variable2test))
    str_variable2test =  "@univ-corse.fr"
    print("QUATRIEME TEST : {} email valide resultat doit etre  (0,1).  RESULTAT = ".format(str_variable2test),is_mail(str_variable2test))
#saisie_full_name()
test_is_mail()