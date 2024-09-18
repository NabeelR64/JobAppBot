from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import os

# Make sure your OpenAI API key is stored as an environment variable

def suggest_job_roles(resume_text):
    prompt = f"Based on the following resume, suggest job roles that the person might be suited for:\n\n{resume_text}"

    try:
        response = client.completions.create(engine="text-davinci-003",  # or use gpt-4 if you have access
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7)

        job_roles = response.choices[0].text.strip().split("\n")

        # Clean up and return the list of job roles
        return [role.strip() for role in job_roles if role.strip()]

    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return []
