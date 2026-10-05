import requests


OLLAMA_URL = "http://localhost:11434/api/generate"

# Ollama model already installed on the system
MODEL_NAME = "qwen3:1.7b"


def generate_meal_plan(prompt):

    request_data = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.6
        }
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=request_data,
            timeout=300
        )

        response.raise_for_status()

        result = response.json()

        if "response" not in result:
            return (
                "ERROR: Ollama returned an unexpected response."
            )

        meal_plan = result["response"].strip()

        if not meal_plan:
            return "ERROR: Ollama returned an empty response."

        return meal_plan

    except requests.exceptions.ConnectionError:

        return """
ERROR: Unable to connect to Ollama.

Please check:

1. Ollama is installed.
2. Ollama is running.
3. qwen3:1.7b is installed.

Check installed models:

    ollama list

Test the model:

    ollama run qwen3:1.7b
"""

    except requests.exceptions.Timeout:

        return """
ERROR: Ollama took too long to respond.

Please test the model manually:

    ollama run qwen3:1.7b
"""

    except requests.exceptions.HTTPError as error:

        return f"""
Ollama HTTP Error:

{error}
"""

    except requests.exceptions.RequestException as error:

        return f"""
Ollama Request Error:

{error}
"""

    except Exception as error:

        return f"""
Unexpected Error:

{error}
"""