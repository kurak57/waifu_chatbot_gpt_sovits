from config import LLM_CLIENT, chat_history

def get_ai_response(command):
    """Sends user input to LLM with chat history and retrieves the response."""
    global chat_history

    # Append user input to history
    chat_history.append({"role": "user", "content": command})

    # Send request to LLM
    completion = LLM_CLIENT.chat.completions.create(
        model="model-identifier",
        messages=chat_history,
        temperature=0.7,
    )

    response = completion.choices[0].message.content

    # Append AI response to history
    chat_history.append({"role": "assistant", "content": response})

    # Limit chat history to the last 20 exchanges
    if len(chat_history) > 20:
        chat_history = [chat_history[0]] + chat_history[-19:]

    return response
