# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
# 
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionFaqSpread(Action):
    def name(self) -> Text:
        return "action_faq_spread"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        Link = "https://www.youtube.com/embed/9Ay4u7OYOhA"
        dispatcher.utter_template("utter_faq_spread", tracker, link=Link)
        return []

class ActionFaqSymptoms(Action):
    def name(self) -> Text:
        return "action_faq_symptoms"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        Link = "https://www.youtube.com/embed/5DGwOJXSxqg"
        dispatcher.utter_template("utter_faq_symptoms", tracker, link=Link)
        return []

class ActionFaqStatus(Action):
    def name(self) -> Text:
        return "action_faq_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        Link = "https://www.youtube.com/embed/NMre6IAAAiU"
        dispatcher.utter_template("utter_faq_status", tracker, link=Link)
        return []
