# 0 Bound, 1 Date + Time, 2 Seq No, 3 Lane, 4 Speed, 5 Class, 6 No of Axle, [ Axle Weight, Axle Spacing]
import sys
from datetime import datetime
import openpyxl
import seaborn as sns
import matplotlib.pyplot as plt

class traffic_data:
      def __init__(traffic_data, Bound, Date_and_Time, Seq_No, Lane, Speed, Class, No_of_Axle, list_of_axle_weight_and_spacing):
        traffic_data.Bound = Bound
        traffic_data.Date_and_Time = Date_and_Time
        traffic_data.Seq_No = Seq_No
        traffic_data.Lane = Lane
        traffic_data.Speed = Speed
        traffic_data.Class = Class
        traffic_data.No_of_Axle = No_of_Axle
        traffic_data.list_of_axle_weight_and_spacing = list_of_axle_weight_and_spacing


#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()
def find_time(entry:list,other_entry:list):
    # date_and_time = date_and_time[1][-8:]
    date_obj1 = datetime.strptime(entry[1][-8:], '%H:%M:%S')
    date_obj2 = datetime.strptime(other_entry[1][-8:], '%H:%M:%S')
    # print(date_obj1,date_obj2)
    output = date_obj2 - date_obj1
    output = output.total_seconds()
    return output

def find_gap(traffic_data: list):
    output = []
    for index, entry in enumerate(traffic_data):
        bound = entry[0]
        if index+1 >= len(traffic_data):
            
            break
        for other_entry in traffic_data[index+1:]:
            if other_entry[0] == bound:
                # print(entry,other_entry)
                time_difference = find_time(entry,other_entry)
                break
        
        # print(target_time)
        # print(type(target_time))
        # time_difference = target_time - base_time
        # print(time_difference,entry[4])
        if time_difference % 1 == 0:
            time_difference = 0.5
        gap_distance = float(time_difference) * (float(entry[4]) /3.6)
        # if index == 2: 
        #     sys.exit()
        if gap_distance == 0:
            continue
        # print(gap_distance)
        output.append([entry, format(gap_distance,".2f")])
        # output.append([entry[5], format(gap_distance,".2f")])
    # print(output)
    return output



def split_bound(traffic_data: list): 
    traffic_bound_1 = []
    traffic_bound_2 = []
    for entry in traffic_data:
        if entry == ['']:
            continue
        if int(entry[0]) == 1:
            traffic_bound_1.append(entry)
        else:
            traffic_bound_2.append(entry)
    return traffic_bound_1, traffic_bound_2


file_names = ['tkb_wim-00aug23-1400 copy','tkb_wim-00aug23-2100 copy','tkb_wim-00nov21-1400 copy','tkb_wim-00nov21-2100 copy','tkb_wim-00nov21-2200 copy','tkb_wim-00nov22-0800 copy','tkb_wim-04dec30-0000 copy','tkb_wim-04dec30-0100 copy','tkb_wim-04dec30-0200 copy','tkb_wim-04dec30-0900 copy','tkb_wim-04dec30-1000 copy','tkb_wim-04dec30-1100 copy','tkb_wim-04dec30-1200 copy','tkb_wim-04dec30-1300 copy','tkb_wim-04dec30-1400 copy','tkb_wim-04dec30-1500 copy','tkb_wim-04dec30-1600 copy','tkb_wim-04dec30-1700 copy','tkb_wim-04dec30-1800 copy','tkb_wim-04dec30-1900 copy','tkb_wim-04dec30-2000 copy','tkb_wim-04dec30-2100 copy','tkb_wim-04dec30-2200 copy','tkb_wim-04dec30-2300 copy','tkb_win-00aug23-2100 copy']
output = []
for file_name in file_names: 
    print('now in: '+file_name)
    path = 'Final Year Project/WIM data/' + file_name + '.csv'
    with open(path,'r') as f: 
        txt = f.read()
    pointer = 6
    txt = txt.split("\n")
    for index, group in enumerate(txt):
        txt[index] = group.split(',')
    traffic_bound_1, traffic_bound_2 = split_bound(txt)
    # print(txt)

    
    tmp1 = find_gap(traffic_bound_1)
    tmp2 = find_gap(traffic_bound_2)

    output = output + tmp1
    output = output + tmp2
    print(len(output))

# [0-9]+-[A-z]+-[0-9]+ +[0-9]+:[0-9]+:[0-9]+

# my_wb = openpyxl.Workbook()
# my_sheet = my_wb.active

# for index, item in enumerate(output): 
#     # print(item)
#     # sys.exit()
#     index += 1
#     my_sheet.cell(row = index, column = 1 ).value = item[0][4]
#     my_sheet.cell(row = index, column = 2 ).value = item[1]


# my_wb.save('Final Year Project/output.xlsx')

x_data = []
y_data = []
for item in output: 
    x_data.append(item[0])
    y_data.append(item[1])

#* Testing!!  
df = sns.load_dataset('iris')
 
# use the function regplot to make a scatterplot
sns.scatterplot(x=x_data,y=y_data)
 
# make a scatterplot without regression fit
#ax = sns.regplot(x=df["sepal_length"], y=df["sepal_width"], fit_reg=False)

plt.show()
sys.exit()



