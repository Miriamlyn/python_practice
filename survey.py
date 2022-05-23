class AnonymousSurvey:
    """collect answers for surveys"""

    def __init__(self, question):
        """store  question and prepare to store answers"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Show survey question"""
        print(self.question)

    def store_response(self, new_response):
        """store responses"""
        self.responses.append(new_response)

    def show_response(self):
        """show responses from survey"""
        print('Survey Results:')
        for response in self.responses:
            print(f"-{response}")
            