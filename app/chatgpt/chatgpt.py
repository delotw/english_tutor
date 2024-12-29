from openai import OpenAI
from settings import CHATGPT_API
from settings import CHATGPT_CONTEXT_37
from gpt_functions import get_context

client = OpenAI(api_key=CHATGPT_API)

context = str(get_context(CHATGPT_CONTEXT_37))

prompt = '''Задание, по которому школьнки писал письмо: You have received a letter from your English-speaking pen friend Steve who writes:
… At school we are doing projects on reading habits of people in different countries. Do you enjoy reading? Who is your favourite writer? Could you tell me what kind of books you and your parents like reading?
As for the family news, my sister got married last week…
Write a letter to Steve.
In your letter
– answer his questions
– ask 3 questions about his sister’s husband
Write 100-140 words.
Само письмо школьника:
Moscow
Russia
10 June
Dear Steve,
Thanks a lot for your letter. I haven’t heard from you for ages. I’m sorry I haven’t answered earlier but I was  busy with my school.
In your letter you asked me about the reading habits in my family. Well, my parents usually read modern novels. However, they wouldn’t mind reading about the life of well-known people.  As for me, I enjoy reading and I read a lot in my spare time. I’m fond of detective stories because they have interesting story lines. My favourite writer is Agatha Christie because her stories are always fascinating. 
Anyway, I’m glad your sister got married. How old is your husband? Is he a student? What kind of music does he enjoy?
I’m sorry, I have to go now as I promised my mum to go shopping with her. 
Please write back!
All the best,
Ivan'''

prompt1 = '''Dear Ronny,
Thank you for the e-mail. It’s always nice to hear from you!
In your previous message you asked me about the weather in summer. It can be quite dry and hot in the south, and rather cool in the north of the country. As for me, I love summer most of all because of my summer vacations. That's the best time for me to go fishing and camping. I'm travelling to St Petersburg this summer. I hope to visit the Hermitage at last and enjoy the places of interest in the city.
You mentioned your uncle Keith. How old is he? Is he coming to see you alone or with his family? What's the purpose of his visit?
Give my best to your parents. Take care and keep in touch!
Best wishes,
Anatoly
'''
