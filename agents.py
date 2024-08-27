from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools


class MarketingAgents:
    def __init__(self):
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def expert_marketing_agent(self):
        return Agent(
            role="Expert en stratégie Marketing dans l'industrie du camping",
            backstory=dedent(f"""Je suis un expert dans la définition de campagne marketing et commerciale,
                            avec une expérience de plusieurs dizaines d'année dans l'industrie du camping"""),
            goal=dedent(f"""Créer un plan détaillé d'action marketing pour la période considérée
                            tenant compte des saisons, météo, bulletin d'enneigement et de la clientèle
                            potentielle correspondante, de l'état de la concurrence et de son niveau de réservation,
                            des évènements sportifs et culturels locaux, des événements à créer,
                            de tes connaissances en marketing pour ce secteur d'activité, afin d'augmenter
                            le chiffre d'affaire du camping La Cascade à Bourg d'Oisans
                            """),
            tools=[
                SearchTools.search_internet,
                ],
            verbose=True,
            allow_delegation=True,
            llm=self.OpenAIGPT4,
            max_iter=8
        )

    def meteo_expert_agent(self):
        return Agent(
            role="synthétiser les prévisions météorologiques de la période",
            backstory=dedent(f"""Je suis un expert dans les données météorologiques de la région depuis des années"""),
            goal=dedent(f"""Rechercher sur le web les prévisions météo pour une date lointaine est peu fiable. Aussi
             tu iras chercher pour la période demandée l'historique des 3 dernières années de la région pour sortir
             une moyenne de synthèse et si la période est en hiver, la moyenne du bulletin d'enneigement des stations
            de l'Alpe d'Huez et des  Deux-Alpes pour faire une synthèse"""),
            tools=[
                SearchTools.search_internet,
                CalculatorTools.calculate
            ],
            verbose=True,
            llm=self.OpenAIGPT4,
            max_iter=5
        )

    def events_expert_agent(self):
        return Agent(
            role="Expert en recherche d'événements sportifs ou culturels",
            backstory=dedent(f"""Je suis un expert dans la recherche d'événements sportifs
             ou culturels locaux,
             avec une expérience de plusieurs dizaines d'année"""),
            goal=dedent(f"""Synthétiser la recherche d'événements sportifs ou culturels locaux,
                            pour les villes de Bourg d'Oisans, l'Alpe d'Huez, les Deux-alpes,
                           """),
            tools=[
                SearchTools.search_internet
                ],
            verbose=True,
            max_iter=5,
            llm=self.OpenAIGPT4,
        )

    def concurrency_expert_agent(self):
        return Agent(
            role="Expert en analyse de concurrence dans l'industrie du camping ",
            backstory=dedent(f"""Je suis un expert dans l'analyse de la concurrence
                                dans les campings de la région de Bourg d'Oisans,
                                avec une expérience de plusieurs dizaines d'année"""),
            goal=dedent(f"""Créer un rapport de synthèse sur l'état de la concurrence,
                            des réservations d'emplacements du camping la Cascade à Bourg d'Oisans
                            , je suis capable de comparer le prix des emplacements de caravanes ou
                             des chalets des campings concurrents 
                            afin de proposer des grilles de tarification optimales pour les différents
                            emplacements du camping."""),
            tools=[
                SearchTools.search_internet,
                CalculatorTools.calculate

                ],
            verbose=True,
            max_iter=5,
            llm=self.OpenAIGPT4,
        )
