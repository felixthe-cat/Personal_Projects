
from curses.ascii import isalpha, isupper


def main():
    with open('Part-Time_RA_CEG_Questions','r') as Questions:
        content = Questions.read()
        question_list = content.split('\n')
        # print(question_list)
        new_question_list = []
        for question in question_list:
            if question != '':
                if ':' not in question:
                    if '(' not in question:
                        new_question_list.append(question.strip())
        for index, question in enumerate(new_question_list):
            if question[-1] != '?':
                new_question_list[index] = question + '?'
        for index, question in enumerate(new_question_list):
            if isalpha(question[0]):
                new_question_list[index] = question[0].upper() + question[1:]
        print(new_question_list)
    with open ('Part-Time_RA_CEG_Questions_Output','w') as Answers:
        for question in new_question_list:
            Answers.write( " :::: " + question + ' {} \n\n')
            # Answers.write()

            


    return

main()