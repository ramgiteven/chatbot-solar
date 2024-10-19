import json
import time

class chatbot_service:
    def __init__(self, openai_repository, get_solar_potential, parse_financial_analisis, saveDataCustomer):
        self.openai_repository = openai_repository
        self.get_solar_potential = get_solar_potential
        self.parse_financial_analisis = parse_financial_analisis
        self.saveDataCustomer = saveDataCustomer
        self.client = self.openai_repository.get_openai_client()

    def start_conversation(self):
        """
        Inicia una nueva conversación en OpenAI.
        """
        thread = self.client.beta.threads.create()
        return thread.id

    def process_message(self, thread_id, user_input):
        """
        Procesa el mensaje del usuario y devuelve la respuesta del asistente.
        """
        self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=user_input
        )

        assistant_id = self.get_assistant_id() 
        run = self.client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id
        )

        while True:
            run_status = self.client.beta.threads.runs.retrieve(
                thread_id=thread_id, run_id=run.id
            )
            if run_status.status == 'completed':
                break
            elif run_status.status == 'requires_action':
                for tool_call in run_status.required_action.submit_tool_outputs.tool_calls:
                    print(run_status.required_action.submit_tool_outputs.tool_calls)
                    if tool_call.function.name == "solar_panel_calculations":
                        output = None
                        arguments = json.loads(tool_call.function.arguments)
                        
                        solarPotential = self.get_solar_potential.execute(arguments["address"], arguments["monthly_bill"])
                        
                        if not isinstance(solarPotential, list) and solarPotential.get("error"):
                            print(solarPotential, "solarPotential")
                            output = solarPotential.get("error")
                        
                        
                        print("solarPotential if final", output)

                        if solarPotential and not output:
                           output = self.parse_financial_analisis.execute(arguments["monthly_bill"], solarPotential)
                        
                        self.client.beta.threads.runs.submit_tool_outputs(thread_id=thread_id,
                                                                    run_id=run.id,
                                                                    tool_outputs=[{
                                                                        "tool_call_id":
                                                                        tool_call.id,
                                                                        "output":
                                                                        json.dumps(output)
                                                                    }])
                    elif tool_call.function.name == "create_contact":
                        arguments = json.loads(tool_call.function.arguments)
                        output = self.saveDataCustomer.execute(arguments["name"], arguments["phone"],
                                                        arguments["address"])
                        self.client.beta.threads.runs.submit_tool_outputs(thread_id=thread_id,
                                                                    run_id=run.id,
                                                                    tool_outputs=[{
                                                                        "tool_call_id":
                                                                        tool_call.id,
                                                                        "output":
                                                                        json.dumps(output)
                                                                    }])

                    time.sleep(1)

        messages = self.client.beta.threads.messages.list(thread_id=thread_id)
        response = messages.data[0].content[0].text.value
        print(f"Assistant response: {response}")
        return response

    def get_assistant_id(self):
        """
        Obtener el ID del asistente, llamando al método `create_assistant` del repositorio.
        """
        assistant_id = self.openai_repository.create_assistant()
        return assistant_id


    def cancel_run(self, thread_id, run_id):
        """
        Cancela el run en OpenAI usando thread_id y run_id.
        """
        return self.openai_repository.cancel_run(thread_id, run_id)