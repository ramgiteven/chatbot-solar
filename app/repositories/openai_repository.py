import os
import openai
import json
import requests
from app.prompts.prompts import formatter_prompt, assistant_instructions,tools_configurations, model_llm, format_message


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
        Obtener cliente de OpenAI
        """
        return openai

    def create_assistant(client):
        """
        Crear asistente o obtener uno si existe
        """
        assistant_file_path = 'assistant.json'

        if os.path.exists(assistant_file_path):
            with open(assistant_file_path, 'r') as file:
                assistant_data = json.load(file)
                assistant_id = assistant_data['assistant_id']
                print("ID de asistente existente cargado.")
        else:
            vector_store = openai.beta.vector_stores.create(name="knowledge_data")
            
            file_paths = ["solar_knowledge.docx"]
            file_streams = [open(path, "rb") for path in file_paths]

            file_batch = openai.beta.vector_stores.file_batches.upload_and_poll(
                vector_store_id=vector_store.id, 
                files=file_streams
            )

            print(f"Estado del lote de archivos: {file_batch.status}")

            if file_batch.status != "completed":
                raise ValueError("La carga de archivos falló o está incompleta.")
            
            assistant = openai.beta.assistants.create(
                instructions=assistant_instructions,
                model=model_llm,
                tools=tools_configurations,
                tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}}
            )

            with open(assistant_file_path, 'w') as file:
                json.dump({'assistant_id': assistant.id}, file)
                print("Se creó un nuevo asistente y se guardó el ID.")

            assistant_id = assistant.id

        return assistant_id
    
    def cancel_run(self, thread_id, run_id):
        """
        Cancelar thread_id y run_id.
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
            raise Exception(f"No se pudo cancelar la ejecución: {response.status_code}, {response.text}")

    def simplify_financial_data_with_gpt(self, data):
        """
        Simplificar datos financieros
        """
        try:
            data_str = json.dumps(data, indent=2)

            system_prompt = formatter_prompt

            completion = self.get_openai_client().chat.completions.create(
                model=model_llm,
                messages=[
                    {
                        "role": "system",
                        "content":
                        system_prompt
                    },
                    {
                        "role":
                        "user",
                        "content": format_message(data_str)
                    }
                ],
                temperature=0)
            
            simplified_data = json.loads(json.dumps(completion.choices[0].message.content))
            return simplified_data

        except Exception as e:
            print("Error al simplificar los datos:", e)
            return None
