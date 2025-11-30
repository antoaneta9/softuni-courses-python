class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

while True:
    parts = input()

    if parts == 'Stop':
        break

    sender, receiver, content = parts.split()
    emails.append(Email(sender, receiver, content))

sent_indices = list(map(int, input().split(', ')))
for index in sent_indices:
    emails[index].send()
for email in emails:
    print(email.get_info())






