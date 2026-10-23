import newspaper
import asyncio
import openai
from openai import AsyncOpenAI
from openai import OpenAI
from dotenv import load_dotenv
import os
import asyncio
import time

# Load environment variables
load_dotenv()

import instructor

# Constants
# LLM_PROVIDER chooses where the ideas come from:
#   "ollama" -> runs a model on your own computer (free)
#   "grok"   -> uses the xAI Grok API (needs XAI_API_KEY)
LLM_PROVIDER = os.getenv('LLM_PROVIDER', 'ollama').lower()

if LLM_PROVIDER == 'grok':
    api_key = os.getenv('XAI_API_KEY')
    if not api_key:
        raise ValueError("Please set XAI_API_KEY in .env file to use Grok.")
    base_url = "https://api.x.ai/v1"
    MODEL_FUNCTION = os.getenv('GROK_MODEL', 'grok-3-mini')
    instructor_mode = instructor.Mode.TOOLS
elif LLM_PROVIDER == 'ollama':
    # Ollama does not check the key, but the client still needs a value
    api_key = "ollama"
    base_url = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434/v1')
    MODEL_FUNCTION = os.getenv('OLLAMA_MODEL', 'llama3.1')
    instructor_mode = instructor.Mode.JSON
else:
    raise ValueError("LLM_PROVIDER must be 'grok' or 'ollama'.")

# Both Grok and Ollama speak the OpenAI API format, so the same client works
async_openai_client = AsyncOpenAI(
    api_key=api_key,
    base_url=base_url,
)
instructor.apatch(async_openai_client, mode=instructor_mode)


def get_article_from_url(url):
    try:
        # Scrape the web page for content using newspaper
        article = newspaper.Article(url)
        # Download the article's content with a timeout of 10 seconds
        article.download()
        # Check if the download was successful before parsing the article
        if article.download_state == 2:
            article.parse()
            # Get the main text content of the article
            article_text = article.text
            return article_text
        else:
            print("Error: Unable to download article from URL:", url)
            return None
    except Exception as e:
        print("An error occurred while processing the URL:", url)
        print(str(e))
        return None

MAX_RETRIES = 3
RETRY_DELAY = 2



async def generate_ideas(user_prompt,response_model):
    """Generates a response using the selected LLM provider (Grok or Ollama)."""
    response = None

    for attempt in range(MAX_RETRIES):
        try:
            resut: response_model = await async_openai_client.chat.completions.create(
                model=MODEL_FUNCTION,
                response_model=response_model,
                messages=[{"role": "user", "content": user_prompt}]
            )

            return resut
        except Exception as e:
            if attempt < MAX_RETRIES - 1:  # don't wait after the last attempt
                await asyncio.sleep(RETRY_DELAY * (2**attempt))
            else:
                print(f"generate_ideas failes after max retries: {e}")
                return None

        return response

