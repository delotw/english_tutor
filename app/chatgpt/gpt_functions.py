from openai import AsyncOpenAI


# ?Функция для получения контекста-методички, чтобы gpt мог оценивать письма
def get_context(path: str):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as err:
        print(f'Не получилось получить файл из-за {err}')


# ?Функция получения ответа от GPT
async def get_score(api: str, context_path: str, mail_text: str):
    context = get_context(context_path)
    client = AsyncOpenAI(api_key=api)
    response = await client.chat.completions.create(
        model='o1-mini',
        messages=[
            {"role": "user",
             "content": context},  # type: ignore
            {"role": "assistant",
             "content": "Хорошо, я готов оценивать письма, согласно критериям, которые ты мне отправил. Я жду письмо."
             },
            {"role": "user",
             "content": mail_text}
        ]
    )
    return response.choices[0].message.content
