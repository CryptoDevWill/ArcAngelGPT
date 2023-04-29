import spacy
from functions.play_sound import play_sound
from engine.question import question

def arc(prompt, chat_window):
    # Load ArcAngel 2.0.0
    nlp = spacy.load('models/arc_output')
    doc = nlp(prompt)
    cats = doc.cats
    prompt_action = max(cats, key=cats.get)
    filter_prompt(prompt, prompt_action, chat_window)


def filter_prompt(prompt, prompt_action, chat_window):
    if prompt_action == 'peery':
        print('perry mode')
    if prompt_action == 'question':
        question(prompt, chat_window)
    if prompt_action == 'command':
        print('command')
