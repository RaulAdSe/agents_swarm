from swarm import Swarm, Agent
from swarm.types import Result
from swarm.repl import run_demo_loop
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create the Swarm client
client = Swarm()

# Define utility functions for context updates and handoffs
def update_business_focus(context_variables, focus_area: str):
    """Updates the current business focus area being discussed"""
    return Result(
        value=f"Switching focus to {focus_area}",
        context_variables={"current_focus": focus_area}
    )

# Define handoff functions for all agents
def transfer_to_legal(): return legal_agent
def transfer_to_market(): return market_agent
def transfer_to_strategy(): return strategy_agent
def transfer_to_academic(): return academic_agent
def transfer_to_financial(): return financial_agent
def transfer_to_international(): return international_agent
def transfer_to_career(): return career_agent

# Create a list of all transfer functions for collaborative capabilities
transfer_functions = [
    transfer_to_legal, transfer_to_market, transfer_to_strategy,
    transfer_to_academic, transfer_to_financial, transfer_to_international,
    transfer_to_career
]

coordinator_agent = Agent(
    name="Coordinator",
    instructions="""You are the main coordinator for an education consulting startup.
    Your role is to:
    1. Understand the initial request/question
    2. Determine which specialized agent(s) should handle it
    3. Transfer to the appropriate agent(s)
    4. Synthesize insights from multiple agents when needed
    
    Start by introducing yourself and asking how you can help with education consulting needs.
    You can collaborate with multiple agents to provide comprehensive answers.""",
    functions=[*transfer_functions, update_business_focus]
)

legal_agent = Agent(
    name="Legal Analyst",
    instructions="""You are a legal analysis specialist focusing on:
    - Education regulatory compliance
    - Student visa regulations
    - Data privacy for student information
    - Contract requirements
    - Liability considerations
    - Required licenses and certifications
    
    Collaborate with other agents when needed for comprehensive solutions.""",
    functions=[*transfer_functions, update_business_focus]
)

market_agent = Agent(
    name="Market Analyst",
    instructions="""You are a market analysis specialist focusing on:
    - Education consulting market analysis
    - Competitor analysis
    - Target audience needs
    - Pricing strategies
    - Service differentiation
    - Regional market variations
    - Growth trends
    
    Collaborate with other agents when needed for comprehensive solutions.""",
    functions=[*transfer_functions, update_business_focus]
)

strategy_agent = Agent(
    name="Strategy Advisor",
    instructions="""You are a strategy advisor focusing on:
    - Business model development
    - Service optimization
    - Growth planning
    - Resource allocation
    - Technology integration
    - Partnership development
    - Revenue strategies
    
    Collaborate with other agents when needed for comprehensive solutions.""",
    functions=[*transfer_functions, update_business_focus]
)

academic_agent = Agent(
    name="Academic Advisor",
    instructions="""You are an academic advisor focusing on:
    - Program selection and requirements
    - University rankings and reputation
    - Admission requirements
    - Application processes
    - Course curriculum analysis
    - Faculty evaluation
    - Academic prerequisites
    
    Help students align their interests with appropriate academic programs.
    Collaborate with other agents when needed for comprehensive solutions.""",
    functions=[*transfer_functions, update_business_focus]
)

financial_agent = Agent(
    name="Financial Advisor",
    instructions="""You are a financial advisor focusing on:
    - Education costs analysis
    - Scholarship opportunities
    - Financial aid guidance
    - Living expenses planning
    - Budget management
    - Payment plans
    - Financial documentation
    
    Help students understand and plan for the financial aspects of their education.
    Collaborate with other agents when needed for comprehensive solutions.""",
    functions=[*transfer_functions, update_business_focus]
)

international_agent = Agent(
    name="International Student Specialist",
    instructions="""You are an international student specialist focusing on:
    - Visa requirements and processes
    - Cultural adaptation
    - Language requirements
    - International admission requirements
    - Housing for international students
    - Cultural integration support
    - Local customs and practices
    
    Help international students navigate the complexities of studying abroad.
    Collaborate with other agents when needed for comprehensive solutions.""",
    functions=[*transfer_functions, update_business_focus]
)

career_agent = Agent(
    name="Career Counselor",
    instructions="""You are a career counselor focusing on:
    - Career path analysis
    - Industry trends
    - Employment prospects
    - Skills alignment
    - Professional development
    - Internship opportunities
    - Alumni success stories
    
    Help students align their education choices with career goals.
    Collaborate with other agents when needed for comprehensive solutions.""",
    functions=[*transfer_functions, update_business_focus]
)

if __name__ == "__main__":
    initial_message = """Welcome to the Education Consulting System!
    
    We can help you with:
    - Academic program selection and requirements
    - Financial planning and scholarships
    - International student services
    - Career counseling and planning
    - Market analysis and trends
    - Legal and regulatory compliance
    - Strategic business planning
    
    How can we assist you today?"""
    
    print(initial_message)
    print("\n" + "="*50 + "\n")
    
    run_demo_loop(
        coordinator_agent,
        context_variables={
            "service_type": "education_consulting",
            "target_audience": "pre_university_students"
        },
        stream=True
    )