from crewai import Task
from textwrap import dedent


class MarketingPlanTasks:
    def __tip_section(self):
        return "Si le plan Marketing est efficace, tu auras une prime de 1000 €!"

    def get_meteo_forecast_task(self, agent, period):
        return Task(
            description=dedent(
                f"""
                **Task**: rechercher les prévisions météorologiques pour la période donnée dans le villes demandée.
                **Description**: Les prévisions météorologiques de la zone sont importantes sur l'enneigement
                 de stations l'hiver et le beau temps lors de la saison non skiable.
                La fréquentation des campings dépend du niveau d'enneigement des stations de novembre à avril, 
                alors qu'au printemps, été et automne le beau temps favorise l'arrivée de campeurs
                venus faire des promenades en altitude ou du vélo.
                **Parameters**:
                - les villes : {"Bourg d'Oisans", "Alpe d'Huez", "les deux-Alpes"}
                - la période :{period}
                **Notes**: {self.__tip_section()}
                """
            ),
            agent=agent,
            expected_output="Synthèse détaillée des prévisions météorologiques pour la période."
        )

    def get_sportive_and_cultural_events_task(self, agent, period):
        return Task(
            description=dedent(
                f"""
                **Task**: compiler les événements sportifs et culturels.
                **Description**: interroger les sites des mairies, les syndicats
                 initiatives de villes concernées pour lister les événements qui sont
                 programmés dans la période passée en paramètre. Il est entendu que le succès
                 de ces événements conditionne la fréquentation des touristes et peuvent être
                 apporteur de clientèle pour le camping. Les courses cyclistes de grande renommée
                comme le tour de FRANCE HOMME OU FEMME, les diverses courses régionales occasionnent
                un regain d'activité pour héberger les sportifs, les médias, les spectateurs.              
                **Parameters**:
                - les villes : {"Bourg d'Oisans", "Alpe d'Huez", "les deux-Alpes"}
                - la période :{period}
                **Notes**: {self.__tip_section()}
                """
            ),
            agent=agent,
            expected_output="Description détaillée des événements sportifs et culturels de la période donnée en paramètre pour les villes passées en paramètres."
        )

    def create_marketing_plan_task(self, agent, period, customer_type, channels):
        return Task(
            description=dedent(
                f"""
                **Task**: Faire des propositions d'action marketing pour la période donnée
                **Description**: le camping de la Cascade est situé sur la commune de Bourg d'Oisans
                dans l'Isère. Les renseignements détaillés sont sur le site  : https://www.campinglacascade.com,
                il comprend 100 emplacements de camping, tente, caravane et camping-car,                
                8 chalets grand confort 35m2, 8 chalets confort 30m2, 6 places maximum.
                Un bâtiment d'accueil est à l'entrée, deux bâtiments sanitaires de grand confort et une piscine 
                avec terrasse pour un snack.
                La clientèle l'hiver se compose de touristes venus skier, d'employés des stations à l'Alpe d'Huez
                ou des Deux_Alpes. La clientèle d'été se compose de campeurs saisonniers, de randonneurs,
                de cyclistes ou d'employés pour les événements culturels et sportifs locaux.
                La tâche consiste à proposer des actions commerciales et marketing pour améliorer
                le nombre d'emplacement vendus pour la période passe en paramètre.                
                **Parameters**:
                - la période :{period}
                - le type de clientèle : {customer_type}
                - les canaux de communication préférés : {channels}
                **Notes**: {self.__tip_section()}
                """,
            ),
            agent=agent,
            expected_output="Description détaillée des actions marketing et commerciales à mener pour augmenter l'activité du camping."
        )

    def analyse_concurrency_task(self, agent, period):
        return Task(
            description=dedent(
                f"""
                        **Task**: établir, pour la période considérée, les prévisions des concurrence pour le camping à Bourg d'Oisans.
                        **Description**: Rechercher sur les sites des syndicats ou fédérations de camping,
                        autour de Bourg d'Oisans les données de prévisions de fréquentation,
                        l'état des réservations, des disponibilité de places, les niveaux de prix des différents
                        type de nuitée.                        
                        **Parameters**:
                        - {period}
                        **Notes**: {self.__tip_section()}
                        """,
            ),
            agent=agent,
            expected_output="Description détaillée de l'itinéraire de 7 jours, incluant des plans quotidiens, hébergements, et activités."
        )
