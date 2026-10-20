from crewai import Task
from tools import tool
from agents import researcher, news_researcher, writing_agent

research_task = Task(
    description=(
        "Analyze the latest news and findings about {topic} collected "
        "by the News Researcher. Identify groundbreaking technologies, "
        "emerging trends, and important innovations. Evaluate their "
        "significance, potential applications, benefits, and limitations. "
        "Compare findings from different sources and prioritize the "
        "innovations with the greatest potential impact. Use evidence "
        "from the research findings and avoid unsupported claims."
    ),
    expected_output=(
        "A detailed research report identifying key technological "
        "breakthroughs, emerging trends, supporting evidence, source "
        "URLs, potential applications, and the significance of each "
        "innovation."
    ),
    tools=[tool],

    agent=researcher
)
news_task = Task(
    description=(
        "Research the latest news and trends about {topic}. "
        "Search reliable and up-to-date sources to find relevant "
        "announcements, technological developments, and industry news. "
        "Collect at least 5 recent news stories, preferably published "
        "within the last 7 days. For each story, provide the headline, "
        "publication date, source URL, a concise summary, and the key "
        "facts. Prioritize credible sources and do not invent news, "
        "dates, or source links."
    ),
    expected_output=(
        "A structured list of at least 5 recent news stories about "
        "{topic}, each containing a headline, publication date, source "
        "URL, concise summary, and key facts."
    ),
    tools=[tool],
    agent=news_researcher
)

news_writer_task = Task(
    description=(
        "Write an engaging, informative, and well-structured technology "
        "news article about {topic} using the findings from the News "
        "Researcher and the Senior Researcher. Create a compelling "
        "headline and introduction, organize the main developments "
        "into logical sections, explain technical concepts in simple "
        "language, and highlight the significance of the innovations. "
        "Maintain factual accuracy, preserve relevant dates and source "
        "URLs, avoid unsupported claims and unnecessary repetition, "
        "and finish with a meaningful conclusion about the future "
        "implications of these developments."
    ),
    expected_output=(
        "A polished technology news article with a headline, introduction, "
        "well-organized body sections, relevant source links, and a "
        "conclusion. The article should be readable, informative, "
        "and grounded in the supplied research."
    ),
      tools=[tool],
    agent=writing_agent,
    ASYNC_EXECUTION=False,
    output_file="output/news_article.txt"  #example of output customization
  
)

# Agent 1: News Researcher

# Variable: news_researcher
# - Task: news_task
# - Does: Finds at least five recent news stories, including headlines, dates, summaries, facts, and source URLs.
# - Tools: Web search tool or a news search API.




# Agent 2: Senior Researcher

# Variable: researcher
# - Task: research_task
# - Does: Evaluates findings, identifies groundbreaking technologies, compares evidence, and explains potential impact.
# - Tools: Research/search tools for finding supporting evidence; optionally academic paper search.




# Agent 3: Writer

# Variable: writer
# - Task: news_writer_task
# - Does: Converts the collected news and analysis into an organized article with a headline, introduction, sections, source links, and conclusion.
# - Tools: Usually none required if it receives sufficient research through task context.
