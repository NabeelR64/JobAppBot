from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Make sure your OpenAI API key is stored as an environment variable

def suggest_job_roles(resume_text):
    prompt = f"Based on the following resume, suggest job roles that the person might be suited for:\n\n{resume_text}"

    messages = [
        {"role": "system", "content": "You are a job role suggestion assistant. Return strictly a list of job roles with no additional text. The list should be formatted as such: Job1, Job2, etc..."},
        {"role": "user", "content": f"Based on the following resume, suggest job roles that the person might be suited for:\n\n{resume_text}"}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4",   
            messages=messages,
            max_tokens=150,
            temperature=0.7
            )

        job_roles = response.choices[0].message.content.split(',')
        print(job_roles, "job roelsssssssssss")

        # Clean up and return the list of job roles
        return [role.strip() for role in job_roles if role.strip()]

    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return []
