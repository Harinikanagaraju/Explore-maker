from litellm import completion


def completion_llm(prompt):
    response = completion(
                model="ollama/llama3.2:1b",
                messages = [
                    { "role": "system", "content": (
                        "if the question is about places then display the details about distance,hospitals,petrol bunks,hotel,bus stands,police station."
                    )},

                    { "role": "user" , "content": prompt },

                    {
                        "role": "system","content": (
                        "If the question is not related to the places then don't respond"
                    )},
    
                    { "role": "user", "content": prompt }
        ],
                api_base="http://localhost:11434",
                stream=True
    )
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)
        