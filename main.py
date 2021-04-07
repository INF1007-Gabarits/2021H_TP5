from Ligue import Ligue


def lire_classement(path):
    league = Ligue("National Hockey League")

    # TODO: Lire le fichier classement2019.txt et storer les données dans des objets ligue, division et equipe.

    return league


def lire_match(path, league):
    # TODO: Lire le fichier et ajouter les matchs encore à jouer dans l'objet ligue

    return league


if __name__ == '__main__':
    # Lire les fichiers
    league = lire_classement('./database/classement2019.txt')
    league = lire_match('./database/matchs2019.txt', league)

    # Simuler la ligue
    league.simuler_ligue()

    # TODO: Retirer 3 équipes de la ligue

    # TODO: Ecrire le classement dans un fichier texte
