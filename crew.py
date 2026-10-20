from crewai import Crew, Process
from task import research_task, news_task, news_writer_task
from agents import researcher, news_researcher, writing_agent
crew = Crew(
    agents=[
        researcher,
        news_researcher,
        writing_agent
    ],
    tasks=[
        research_task,
        news_task,
        news_writer_task
    ],
    process=Process.sequential  
)

##starting task execution with enhanced feedback

result=crew.kickoff(inputs={'topic': 'Artificial Intelligence'})
print(result)
