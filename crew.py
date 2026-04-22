from crewai import Crew, Process
from dotenv import load_dotenv
from agent import blog_resercher, writer_agent
from task import research_task, write_task


load_dotenv()

crew = Crew(
    agents=[blog_resercher,writer_agent],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory = True,
    cache = True,
    max_rpm = 100,
    verbose = True
)

result = crew.kickoff(inputs = {'topic': 'technology  TRE4', 'youtube_channel_handle': '@smitadomini'})