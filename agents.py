from crewai import Agent
from tools import tool

from dotenv import load_dotenv
load_dotenv()
from crewai import Agent, LLM

import os
# call model

llm=LLM(
    model="gemini/gemini-3.8-flash",
    temperature=0.5,

    verbose=True,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
#     Temperature	Behavior	                           Example
# 0.0	           More predictable and consistent	       Direct factual answers
# 0.5	           Balanced creativity and consistency	   News summaries and AI agents
# 1.0	          More varied and creative	               Brainstorming ideas

#creating a senior researcher agent iwth memory and verbose mode
# Parameter	          Meaning	                                            Question it answers
# role	              The agent's job title or function	                    Who are you?
# goal	              The task or outcome it must achieve	                  What should you do?
# backstory	          The agent's background, expertise, and perspective	  What experience or knowledge do you have?

researcher=Agent(
    role="Senior Technology Researcher",
    goal="Analyze research findings to identify groundbreaking technologies, evaluate their significance, and uncover the most important innovations in {topic}.",
    verbose=True,
    memory=False,
    # In CrewAI, memory=False means the agent does not use stored information from previous interactions or tasks.
    backstory=(
        "You are an experienced technology researcher with a strong background in computer science, "
    "emerging technologies, and research analysis. You specialize in evaluating technological "
    "breakthroughs, comparing research findings, identifying long-term trends, and understanding "
    "the potential impact of innovations. You critically examine evidence from multiple sources "
    "rather than accepting claims at face value. Your mission is to transform research findings "
    "into meaningful insights and identify technologies that could shape the future."
),
    tools=[tool],
    llm=llm,
    allow_delegation=True,
    #allow_delegation=True The agent can delegate tasks to other agents when the setup supports it.

)

news_researcher=Agent(
   role="Technology News Researcher",
    goal="Discover the latest news, announcements, and emerging trends in {topic} by gathering relevant information from reliable and up-to-date sources.",
    verbose=True,
    memory=False,
    backstory=(
        "You are a dedicated technology news researcher who specializes in tracking the latest "
        "developments across the technology industry. You monitor news sources, research reports, "
        "company announcements, and industry publications to identify relevant updates. You focus "
        "on collecting recent information, recording publication dates, checking source credibility, "
        "and summarizing important facts accurately. You prioritize reliable evidence over speculation "
        "and provide clear, organized research findings that help other team members understand "
    "what is happening in the technology world."
),
tools=[tool],
llm=llm,
  allow_delegation=True,
)

#creating writing agent responsible for writng blogs

writing_agent=Agent(
    role="Technology Content Writer",
    goal="Write clear, engaging, and well-structured technology articles about {topic} using the research findings provided by the other agents, ensuring factual accuracy and readability.",
    verbose=True,
    memory= False,
backstory=(
    "You are an experienced technology content writer who specializes in transforming complex "
    "technical research and breaking news into informative, engaging articles. You excel at "
    "organizing information logically, explaining technical concepts in simple language, and "
    "highlighting the most important findings for readers. You use the research and analysis "
    "provided by other agents to create coherent articles with compelling headlines, clear "
    "introductions, informative body sections, and meaningful conclusions. You preserve factual "
    "accuracy, avoid unsupported claims, and ensure that important facts and source references "
    "are retained. Your mission is to make emerging technologies and the latest developments "
    "easy for readers to understand."
),
tools=[tool],
llm=llm,
  allow_delegation=False,

)

