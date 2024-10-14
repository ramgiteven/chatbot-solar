import os
import openai
import json
import requests
from app.prompts.prompts import formatter_prompt, assistant_instructions


class openai_repository:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')

        if not self.api_key:
            raise ValueError("La variable de entorno 'OPENAI_API_KEY' no está configurada.")

        openai.api_key = self.api_key
        openai.default_headers = {
            "Authorization": f"Bearer {self.api_key}",
            "OpenAI-Beta": "assistants=v2"
        }

    def get_openai_client(self):
        """
            Get Client OpenIA
        """
        return openai

    def create_assistant(client):
        """
            Create assistant or Get One if exists
        """
        assistant_file_path = 'assistant.json'

        if os.path.exists(assistant_file_path):
            with open(assistant_file_path, 'r') as file:
                assistant_data = json.load(file)
                assistant_id = assistant_data['assistant_id']
                print("Loaded existing assistant ID.")
        else:
            vector_store = openai.beta.vector_stores.create(name="knowledge_data")
            
            file_paths = ["knowledge.docx"]
            file_streams = [open(path, "rb") for path in file_paths]

            file_batch = openai.beta.vector_stores.file_batches.upload_and_poll(
                vector_store_id=vector_store.id, 
                files=file_streams
            )

            print(f"File batch status: {file_batch.status}")
            print(f"File batch file counts: {file_batch.file_counts}")

            if file_batch.status != "completed":
                raise ValueError("File upload failed or is incomplete.")
            
            assistant = openai.beta.assistants.create(
                instructions=assistant_instructions,
                model="gpt-4-1106-preview",
                tools=[
                    {
                        "type": "file_search"
                    },
                    {
                        "type": "function",
                        "function": {
                            "name": "solar_panel_calculations",
                            "description": "Calculate solar potential based on a given address and monthly electricity bill in USD.",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "address": {
                                        "type": "string",
                                        "description": "Address for calculating solar potential."
                                    },
                                    "monthly_bill": {
                                        "type": "integer",
                                        "description": "Monthly electricity bill in USD for savings estimation."
                                    }
                                },
                                "required": ["address", "monthly_bill"]
                            }
                        }
                    },
                    {
                        "type": "function",
                        "function": {
                            "name": "create_contact",
                            "description": "Capture contacts details and save to Airtable.",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "type": "string",
                                        "description": "Name of the contact."
                                    },
                                    "phone": {
                                        "type": "string",
                                        "description": "Phone number of the contact."
                                    },
                                    "address": {
                                        "type": "string",
                                        "description": "Address of the contact."
                                    }
                                },
                                "required": ["name", "phone", "address"]
                            }
                        }
                    }
                ],
                tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}}
            )

            with open(assistant_file_path, 'w') as file:
                json.dump({'assistant_id': assistant.id}, file)
                print("Created a new assistant and saved the ID.")

            assistant_id = assistant.id

        return assistant_id
    
    def cancel_run(self, thread_id, run_id):
        """
            Kill thread_id and run_id.
        """
        url = f"https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/cancel"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "OpenAI-Beta": "assistants=v2"
        }

        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to cancel run: {response.status_code}, {response.text}")

    def simplify_financial_data_with_gpt(self, data):
        """
            Simplify financial data
        """
        try:
            data_str = json.dumps(data, indent=2)

            system_prompt = formatter_prompt

            completion = self.get_openai_client().chat.completions.create(
                model="gpt-4-1106-preview",
                messages=[
                    {
                        "role": "system",
                        "content":
                        system_prompt
                    },
                    {
                        "role":
                        "user",
                        "content":
                        f"Here is some data, parse and format it exactly as shown and only return json string not formated like ```json : {data_str}"
                    }
                ],
                temperature=0)
            
            simplified_data = json.loads(completion.choices[0].message.content)
            return simplified_data

        except Exception as e:
            print("Error simplifying data:", e)
            return None
