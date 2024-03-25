# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormValidationAction

class ValidateWelcomeForm(FormValidationAction):
    """Example of a form validation action."""

    def name(self) -> Text:
        return "validate_welcome_form"

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer."""
        try:
            int(string)
            return True
        except ValueError:
            return False
    
    def validate_menu(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        
        if self.is_int(value) and int(value) > 0:
            return {"menu": value}
        else:
            dispatcher.utter_message(Text="salah input")
            # validation failed, set slot to None
            return {"menu": None}

class ActionDataBeratbadan(Action):
    def name(self):
        return "action_data_beratbadan"

    def run(self, dispatcher, tracker, domain):

        jenis_kelamin = tracker.get_slot("jenis_kelamin")
        umur = tracker.get_slot("umur")
        berat_badan = tracker.get_slot("berat_badan")

        if jenis_kelamin == True:
            dispatcher.utter_message(text="Jenis Kelamin: Laki-laki\n")
        else:
             dispatcher.utter_message(text="Jenis Kelamin: Perempuan\n")
        
        if umur & berat_badan > 0:
            dispatcher.utter_message(text="Menyala Abangkuuhh\n")
        else:
            dispatcher.utter_message(text="Input invalid\n")

        return[]


class ActionFeedbackChecklistfirst(Action):
    def name(self):
        return "action_feedback_checklistfirst"

    def run(self, dispatcher, tracker, domain):

        question11 = tracker.get_slot("question11")
        question12 = tracker.get_slot("question12")
        question13 = tracker.get_slot("question13")
        question14 = tracker.get_slot("question14")
        question15 = tracker.get_slot("question15")
        question16 = tracker.get_slot("question16")
        question17 = tracker.get_slot("question17")
        question18 = tracker.get_slot("question18")
        question19 = tracker.get_slot("question19")
        question110 = tracker.get_slot("question110")
        
        
        if question11 == False:
            dispatcher.utter_message(response="utter_response_question11")
        if question12 == False:
            dispatcher.utter_message(response="utter_response_question12")
        if question13 == False:
            dispatcher.utter_message(response="utter_response_question13")
        if question14 == False:
            dispatcher.utter_message(response="utter_response_question14")
        if question15 == False:
            dispatcher.utter_message(response="utter_response_question15")
        if question16 == False:
            dispatcher.utter_message(response="utter_response_question16")
        if question17 == False:
            dispatcher.utter_message(response="utter_response_question17")
        if question18 == False:
            dispatcher.utter_message(response="utter_response_question18")
        if question19 == False:
            dispatcher.utter_message(response="utter_response_question19")
        if question110 == False:
            dispatcher.utter_message(response="utter_response_question110")
            
            return []
    
class ActionFeedbackChecklistsecond(Action):
    def name(self):
        return "action_feedback_checklistsecond"

    def run(self, dispatcher, tracker, domain):

        question21 = tracker.get_slot("question21")
        question22 = tracker.get_slot("question22")
        question23 = tracker.get_slot("question23")
        question24 = tracker.get_slot("question24")
        question25 = tracker.get_slot("question25")
        question26 = tracker.get_slot("question26")
        question27 = tracker.get_slot("question27")
        question28 = tracker.get_slot("question28")
        question29 = tracker.get_slot("question29")
        question210 = tracker.get_slot("question210")
                
        if question21 == False:
            dispatcher.utter_message(response="utter_response_question21")

        if question22 == False:
            dispatcher.utter_message(response="utter_response_question22")

        if question23 == False:
            dispatcher.utter_message(response="utter_response_question23")

        if question24 == False:
            dispatcher.utter_message(response="utter_response_question24")

        if question25 == False:
            dispatcher.utter_message(response="utter_response_question25")

        if question26 == False:
            dispatcher.utter_message(response="utter_response_question26")

        if question27 == False:
            dispatcher.utter_message(response="utter_response_question27")

        if question28 == False:
            dispatcher.utter_message(response="utter_response_question28")

        if question29 == False:
            dispatcher.utter_message(response="utter_response_question29")

        if question210 == False:
            dispatcher.utter_message(response="utter_response_question210")

            return []

# class ValidateChecklistfirstForm(FormValidationAction):
#   def name(self) -> Text:
#       return "validate_checklistfirst_form"

#   @staticmethod
#   def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ):

#         question11 = tracker.get_slot("question11")

#         if question11 == False:
#             return [dispatcher.utter_message(text="Q1 Tidak Normal")]

#         return []

# class ActionSetChecklist(Action):
#     def name(self):
#         return "action_set_checklist"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         intent = tracker.latest_message["intent"].get("name")

#         if intent == "deny":
#             return [dispatcher.utter_message(text="Tidak Normal")]
#         elif intent == "affirm":
#             return [dispatcher.utter_message(text="Normal")]
#         return []
    

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
