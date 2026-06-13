def select_tool(client, user_input):

    tool_prompt = f"""
You are a tool selector.

Available tools:
- get_time
- get_date
- say_hello

User: {user_input}

Reply with ONLY one of:
get_time
get_date
say_hello
none
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": tool_prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()