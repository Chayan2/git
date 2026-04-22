from crewai import Task
from tools import yt_tool
from agent import blog_resercher, writer_agent

#researching task 
research_task = Task(
    description = (
        "Identify the video {topic} from the YouTube channel {youtube_channel_handle}. "
        "Get detailed information about the video from the channel"
    ),
    expected_output = 'A comprehensive 3 paragraphs long report based on the {topic} of video',
    tools = [yt_tool],
    agent = blog_resercher

)

#writing task with language model configuration 
write_task = Task(
    description = (
        "Get information about the video from the youtube channel {youtube_channel_handle} on the topic:{topic}"
    ),
    expected_output = 'Summarize the info from the youtube channel videos on the topic: {topic}',
    tools = [yt_tool],
    agent = writer_agent,
    async_execution=False,
    output_file="output.md"
)