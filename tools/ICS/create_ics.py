from ics import Calendar, Event
from datetime import datetime, timedelta

def creer_evenement_ics(nom, date_debut, duree_heures, description, lieu):
    # Convertir la date de début en objet datetime
    date_debut_obj = datetime.strptime(date_debut, "%Y-%m-%dT%H:%M:%S")
    
    # Calculer la date de fin en ajoutant la durée à la date de début
    date_fin_obj = date_debut_obj + timedelta(hours=duree_heures)
    
    # Créer un événement
    evenement = Event()
    evenement.name = nom
    evenement.begin = date_debut_obj.strftime("%Y-%m-%d %H:%M:%S")
    evenement.end = date_fin_obj.strftime("%Y-%m-%d %H:%M:%S")
    evenement.description = description
    evenement.location = lieu
    
    return evenement

def creer_calendrier_ics(evenements, fichier_ics):
    # Créer un objet calendrier
    cal = Calendar()

    # Ajouter chaque événement au calendrier
    for evenement in evenements:
        cal.events.add(evenement)
    
    # Sauvegarder le calendrier dans un fichier .ics
    with open(fichier_ics, 'w') as f:
        f.writelines(cal)

    print(f"Calendrier avec plusieurs événements enregistré dans {fichier_ics}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Créer une liste d'événements
    evenements = [
        creer_evenement_ics(
            "Réunion d'équipe", "2024-10-05T14:00:00", 1.5,
            "Réunion pour discuter de l'avancement du projet.", 
            "Salle de conférence, Bureau central"
        ),
        creer_evenement_ics(
            "Appel client", "2024-10-06T10:00:00", 0.5,
            "Appel avec un client important.", 
            "Bureau"
        ),
        creer_evenement_ics(
            "Déjeuner avec les collègues", "2024-10-07T12:30:00", 1.0,
            "Déjeuner informel avec l'équipe.",
            "Restaurant du coin"
        )
    ]

    # Créer le fichier .ics avec plusieurs événements
    creer_calendrier_ics(evenements, "calendrier_evenements.ics")
