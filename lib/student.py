class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
    def raise_hand(self):
        print("Pick me!")
class ChattyStudent(Student):
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    def raise_hand(self):
        counter = 0
        while counter < 10:
            print("Pick me!")
            counter += 1

kamau = ChattyStudent()
kamau.raise_hand()

