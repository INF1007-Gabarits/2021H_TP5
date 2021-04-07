from random import normalvariate, randint


class Ligue:
    def __init__(self, nom):
        self.nom = nom
        self.divisions = []
        self.parties_restantes = []


    def simuler_ligue(self):
        for partie in self.parties_restantes:
            abv_equipe_a, abv_equipe_b = partie

            # TODO: Obtenir l'OBJET représentant l'équipe et l'OBJET représentant la division à partir de l'abbréviation
            team_a, division_a =
            team_b, division_b =

            # TODO: Simuler une rencontre
            pts_equipe_a, pts_equipe_b, but_equipe_a, but_equipe_b, vrp_a, vrp_b =


            # TODO: Mettre à jour les statistiques de team_a et team_b
            stats_equipe_a = {'PTS': pts_equipe_a,
                              'BP': but_equipe_a,
                              'BC': but_equipe_b,
                              'VRP': vrp_a}
            stats_equipe_b = {'PTS': pts_equipe_b,
                              'BP': but_equipe_b,
                              'BC': but_equipe_a,
                              'VRP': vrp_b}

        # TODO: Mettre à jour le clasement de chacune des divisions
