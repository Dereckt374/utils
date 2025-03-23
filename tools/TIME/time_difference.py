
import math

def time_difference(date_1, date_2):
    delta = date_2 - date_1
    nb_days = delta.days
    nb_hour = math.floor(delta.seconds / 3600)
    nb_min = math.floor(delta.seconds / 60) - (nb_hour*60)
    nb_seconds = delta.seconds - (nb_hour * 3600) - (nb_min * 60)
    # print(f"nombre total de jours : {round(delta.days + delta.seconds / (24 * 3600),2)}\nnombre total de secondes : {int(delta.total_seconds())}\nnombre total d'heures : {round(delta.total_seconds()/3600,1)}\nnombre total de minutes : {round(delta.total_seconds()/60,1)}")
    print(f'day\t= {nb_days}\nhour\t= {nb_hour}\nminute\t= {nb_min}\nsecond\t= {nb_seconds}')
    return(delta.total_seconds())