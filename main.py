from src.kahvikone import kahvikone
from src.tennistilastot import ATPTourStats


kahvikone(3.65, 400)
kahvikone(2.25, 274.3)

atp_tour_stats = ATPTourStats(tournament_data_filepath='src\\tournaments_2010-2019.csv',
                              match_data_filepath='src\\match-scores_2010-2019.csv')
atp_tour_stats.tournaments_by_year()
atp_tour_stats.tournaments_won_by_players()