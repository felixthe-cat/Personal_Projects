
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
        for index, question in enumerate(question_list):
            print(question[-1] != '?')
            if len(question) == 0:
                print('ARRR')
            # if question[-1] != '?':
                # pass
            #     new_question_list[index] = question + '?'


    return

main()