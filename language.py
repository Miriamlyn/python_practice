from survey import AnonymousSurvey

#define a question, and make a survey
question = "What language did you learn to speak first?"
my_survey = AnonymousSurvey(question)

#show questiona and responses
my_survey.show_question()
print("Enter 'q' to quit. \n")
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

#show results
print("\nThank you everyone for participating in the survey!")
my_survey.show_response()