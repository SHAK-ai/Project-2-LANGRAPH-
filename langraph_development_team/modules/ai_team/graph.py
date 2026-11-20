from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langraph_supervisor import create_supervisor

def create_chat_model():
    return ChatOpenAI(
        model = os.environ["OPENAI_MODEL"],
        base_url = os.getenv("OPENAI_BASE_URL") or None,
        temperature = 0,
        max_retries = 6
    )

def build_team(model = None):
    model = create_chat_model()
    planner = create_agent(
        name = "Planner Sub-Agent",
        model = model,
        tools= [],
        system_prompt = ""
    )