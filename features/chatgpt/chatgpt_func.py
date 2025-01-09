import httpx
from loguru import logger
from openai import AsyncOpenAI, http_client
from dotenv import load_dotenv
import os

from settings import CONTEXT_37
load_dotenv()

API = os.getenv('CHATGPT')
PROXY = os.getenv('PROXY')

client = AsyncOpenAI(api_key=API,
                     http_client=httpx.AsyncClient(
                         proxy=PROXY,
                         transport=httpx.HTTPTransport(local_address="0.0.0.0"))
                     )


# Функция для получения контекста-методички, чтобы gpt мог оценивать письма
def get_context(path: str):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as err:
        print(f'Не получилось получить файл из-за {err}')


# Функция получения ответа от GPT
async def get_score_37(mail_text: str):
    logger.info('Отправляю запрос к ChatGPT')
    context = get_context(CONTEXT_37)

    response = await client.chat.completions.create(
        model='o1-mini',
        messages=[
            {"role": "user",
             "content": context},
            {"role": "assistant",
             "content": "Хорошо, я готов оценивать письма, согласно критериям, которые ты мне отправил. Я жду письмо. И да, не используй разметку MardDown в своих ответах."
             },
            {"role": "user",
             "content": mail_text}
        ]
    )
    logger.success('Получен ответ от ChatGPT')
    return response.choices[0].message.content
