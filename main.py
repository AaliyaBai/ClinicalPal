from clinical_bot import ClinicalChatbot

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout


class ClinicalChatbotApp(App):

    def build(self):
        self.root = BoxLayout(orientation='vertical')

        # ScrollView to hold chat log
        self.scroll_view = ScrollView(size_hint=(1, 0.9))
        self.chat_log = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.chat_log.bind(minimum_height=self.chat_log.setter('height'))
        self.scroll_view.add_widget(self.chat_log)

        # Input box and send button
        self.input_box = BoxLayout(size_hint=(1, 0.1))
        self.text_input = TextInput(hint_text="Type a message", size_hint=(0.8, 1))
        self.send_button = Button(text="Send", size_hint=(0.2, 1))
        self.send_button.bind(on_press=self.send_message)
        self.input_box.add_widget(self.text_input)
        self.input_box.add_widget(self.send_button)

        self.root.add_widget(self.scroll_view)
        self.root.add_widget(self.input_box)

        self.chatbot = ClinicalChatbot("Cindy Orozco")
        greetings = self.chatbot.start_chat()
        self.add_message("Bot: " + greetings, True)

        return self.root

    def send_message(self, instance):
        message = self.text_input.text.strip()
        if message:
            self.add_message("You: " + message, False)
            self.text_input.text = ''
            reply = self.chatbot.send_message(message)
            self.add_message("Bot: " + reply, True)

    def add_message(self, message, is_bot):
        color = (0, 0, 1, 1)
        if is_bot:
            color = (0, 1, 0, 1)
        r, g, b, a = color
        color_hex = f"{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}{int(a * 255):02x}"
        message_label = Label(
            text=f"[color=#{color_hex}]{message}[/color]",
            size_hint_y=None,
            halign='left',
            valign='middle',
            markup=True,
            text_size=(self.scroll_view.width, None)  # Adjust text_size for wrapping
        )
        message_label.bind(size=message_label.setter('text_size'))
        message_label.bind(texture_size=message_label.setter('size'))
        self.chat_log.add_widget(message_label)
        # Scroll to the bottom of the chat log
        self.scroll_view.scroll_y = 0


if __name__ == "__main__":
    ClinicalChatbotApp().run()
