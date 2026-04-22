from crewai import Agent
from tools import yt_tool

# create a senior blog researcher ai
blog_resercher =  Agent(
    role = "Blog Researcher from youtubes videos",
    goal = "Get a relavant video content for the topic: {topic} from YT channel {youtube_channel_handle}",
    verbose = True,
    memory = True,
    backstory = (
        "Expert in understanding videos in AI, Data Science, Machine Learning and GenAi"
    ),
    tools = [yt_tool],
    allow_delegation = True 
     
)

# creating a senior blog writer agent
writer_agent =  Agent(
    role = "Blog Writer",
    goal = "Narrate compelling tech stories about video {topic} from YT channel {youtube_channel_handle}",
    verbose = True,
    memory = True,
    backstory = (
        "With the  fair for simplifying complex topics, you craft"
        "discovries to light in accessable manner"
        "engaging narratives that captivate and educate, bringing now"

    ),
    tools = [yt_tool],
    allow_delegation = True 
     
)