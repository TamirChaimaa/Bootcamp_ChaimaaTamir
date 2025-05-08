#Call History
#Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object create an attribute called call_history which value is an empty list.
class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.call_messages = []
#Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. The method should print a string stating who called who, and add this string to the phone’s call_history.
    def call(self,other_phone):
        call_string = f"{self.phone_number} called {other_phone.phone_number}"
        self.call_history.append(call_string)
        print(call_string)
        return call_string
    
#Add a method called show_call_history. This method should print the call_history.
    def show_call_history(self):
        for call in self.call_history:
            print(call)
#Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
#to : the number of another Phone object
#from : your phone number (also a Phone object)
#content
    def send_message(self, other_phone, content):
       message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
         }     
       self.call_messages.append(message)
       other_phone.call_messages.append(message) 
       return message

#Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)
    def show_outgoing_messages(self):
        print("\nMessages envoyés:")
        for message in self.call_messages:
            if message["from"] == self.phone_number:
                print(f"To: {message['to']} |  Message: {message['content']}")
    
    def show_incoming_messages(self):
        print("\nSent messages:")
        for message in self.call_messages:
            if message["to"] == self.phone_number:
                print(f"From: {message['from']} | Message: {message['content']}")
    
    def show_messages_from(self, phone_number):
        print(f"\nMessages from {phone_number}:")
        for message in self.call_messages:
            if message["from"] == phone_number and message["to"] == self.phone_number:
                print(f"Message: {message['content']}")

if __name__ == "__main__":
    phone1 = Phone("123-456-789")
    phone2 = Phone("987-654-321")
    
    phone1.call(phone2)
    phone2.call(phone1)
    phone1.call(phone2)
    
    phone1.show_call_history()
    
    phone1.send_message(phone2, "Hello! How are you?")
    phone2.send_message(phone1, "I'm very well, thank you! And you?")
    phone1.send_message(phone2, "All good!")
    
    print("\nMessage test for phone1:")
    phone1.show_outgoing_messages()
    phone1.show_incoming_messages()
    phone1.show_messages_from("987-654-321")
    
    print("\nMessage test for phone2:")
    phone2.show_outgoing_messages()
    phone2.show_incoming_messages()
    phone2.show_messages_from("123-456-789")








