import os
from crewai import Crew

from textwrap import dedent
from agents import MarketingAgents
from tasks import MarketingPlanTasks
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")


class MarketingCrew():
    def __init__(self, period, customer_type, marketing_channels):
        self.period = period
        self.customer_type = customer_type
        self.marketing_channels = marketing_channels

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = MarketingAgents()
        tasks = MarketingPlanTasks()

        # Define your custom agents and tasks here
        expert_mkt_agent = agents.expert_marketing_agent()
        meteo_expert_agent = agents.meteo_expert_agent()
        events_expert_agent = agents.events_expert_agent()
        concurrency_expert_agent = agents.concurrency_expert_agent()

        # Custom tasks include agent name and variables as input
        meteo_forecast = tasks.get_meteo_forecast_task(
            meteo_expert_agent,
            self.period
        )

        events_forecast = tasks.get_sportive_and_cultural_events_task(
            events_expert_agent,
            self.period
        )

        analyse_concurrency = tasks.analyse_concurrency_task(
            concurrency_expert_agent,
            self.period,
        )

        create_mkt_report = tasks.create_marketing_plan_task(
            expert_mkt_agent,
            self.period,
            self.customer_type,
            self.marketing_channels
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_mkt_agent, meteo_expert_agent, events_expert_agent, concurrency_expert_agent],

            tasks=[meteo_forecast, events_forecast, analyse_concurrency, create_mkt_report],
            verbose=True,
        )
        proposal = crew.kickoff()
        return proposal



if __name__ == "__main__":
    print("## Bienvenue dans marketing Niellin !!")

    print("-------------------------------")
    month = input(dedent("""pour quel mois à venir, souhaitez avoir un plan marketing ? """))
    customer_type = input(dedent("""quelle clientèle souhaitez vous cibler? """))
    preferred_media = input(dedent("""quels médias souhaitez vous utiliser? """))
    # month = "Janvier 2025"
    # customer_type = "tous"
    # preferred_media = ["réseaux sociaux, site web, mailing"]

    mkt_crew = MarketingCrew(month, customer_type, preferred_media)
    result = mkt_crew.run()
    print("\n\n##########################")
    print("## Ici est votre résultat:")
    print("###########################\n")
    print(result)
