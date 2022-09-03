
from curses.ascii import isalpha, isupper


def main():
    with open('Part-time_RA/Part-Time_RA_Excel_Questions','r') as Questions:
        content = Questions.read()
        question_list = content.split('"')
        # print(question_list)
        new_question_list = []
        for question in question_list:
            if question != '':
                # if ':' not in question:
                #     if '(' not in question:
                new_question_list.append(question.strip())
        print_list(new_question_list)

        # Adding a question mark at the end of the question
        # for index, question in enumerate(new_question_list):
        #     if question[-1] != '?':
        #         new_question_list[index] = question + '?'

        # Capitalising the first Letter of the sentence
        # for index, question in enumerate(new_question_list):
        #     if isalpha(question[0]):
        #         new_question_list[index] = question[0].upper() + question[1:]

        print(new_question_list)
    with open ('Part-time_RA/Part-Time_RA_CEG_Excel_Questions_Output','w') as Answers:
        for index, question in enumerate(new_question_list):
            Answers.write( " :: Excel_Question " + str(index) + " :: " + question + ' {} \n\n')
            # Answers.write()

            


    return

def print_list(question_list: list):
    for question in question_list:
        print(question,end='\n----------------------------\n\n')
    return 

main()