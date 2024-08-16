import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = "Your API-KEY"
def suggest_code(task, language):
    prompt = f"Write code in {language} to {task}"
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use other engines like 'gpt-4' if available
        prompt=prompt,
        max_tokens=150  # Adjust based on how lengthy you want the response to be
    )
    return response.choices[0].text.strip()
def main():
    task = input("What task do you want to accomplish with the code? ")
    language = input("Which programming language do you want to use? ")
    code_suggestion = suggest_code(task, language)
    print(f"Suggested code in {language}:\n{code_suggestion}")
main()