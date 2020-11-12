from transformers import pipeline, AutoTokenizer, AutoModelWithLMHead

from typing import Any, Dict, List, Text, Union
import time
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import BotUttered
from rasa_sdk.events import SlotSet


# Respond with a career response
class action_find_career_response(Action):
    # def name(self) -> Text:
    def name(self):
        return "action_find_career_response"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: "Tracker",
        domain: Any):

        # rasa_slot = tracker.get_slot('test_memory')
        slot = SlotSet(
            key = "test_memory",
            value = "remember this"
        )

        message = BotUttered(
            text = "hello",
            timestamp = time.time())

        message2 = BotUttered(
            text = "hello number 2",
            timestamp = time.time())    
        # dispatcher.utter_message(message) #return as response
        # return []
        return [slot] #return as event
        
class generate_text(Action):
    def name(self)-> Text:
        return "action_generate_text"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: "Tracker",
        domain: Any):
        tokenizer = AutoTokenizer.from_pretrained("gpt2")
        model = AutoModelWithLMHead.from_pretrained("gpt2")
        text_generator = pipeline("text-generation", tokenizer=tokenizer, model=model)
        seed_language = "I'm glad you're interested in this position. Let's chat about"
        generated_text = text_generator(seed_language,max_length=100, do_sample=False)
        
        option1 = SlotSet(
            key = "option1",
            value = generated_text
            # value = generated_test[0]
        )
        # option2 = SlotSet(
        #     key = "option2"
        #     value = generated_test[1]
        # )
        
        # option3 = SlotSet(
        #     key = "option3"
        #     value = generated_test[2]
        # )
        dispatcher.utter_message("It worked. I've generated the following text.") #return as response
        return [option1]