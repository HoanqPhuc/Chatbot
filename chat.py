import openai

openai.api_key = ''

def chat_with_bot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt,              
        max_tokens=150,            
        n=1,                        
        stop=None,                 
        temperature=0.7            
    )

    return response.choices[0].text.strip()

if __name__ == "__main__":
    print("Chatbot đã sẵn sàng! Gõ 'exit' để thoát.")
    while True:
        user_input = input("Bạn: ")
        if user_input.lower() == 'exit':
            break
        response = chat_with_bot(user_input)
        print(f"Chatbot: {response}")