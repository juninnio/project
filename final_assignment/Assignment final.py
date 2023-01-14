
# Assignment : Write a program and analyse informations from AAPL_Group.txt. The information in the file must be extracted and transferred to suitable lists. 
# Analyzed information are to be calculated and outputted in a certain format. The output is also saved in a txt file named reports_s.txt where s is a number returned by int(time.time())
# Program should also be able to visualise the information on liner graphs based on monthly averages of trade volume and monthly averages of closing value.


# Importing Libraries
import time # To get time 
import matplotlib.pyplot as plt # To make line graphs


plt.rc('font', size=6) #Changing chart font size
again = 'y' #Declaring variable for while loop


#Making file_open function to open file and handle errors (File not Found)
def file_open():
    try :
        file_obj = open("D:\Python\School\AAPL_Group.txt","r")
        datas = file_obj.readlines()
        return datas #returning datas list
    except FileNotFoundError:
        print("Error, file not found, please check the file name!") #Error Message resulting in program exiting
        print('Exiting...')
        exit()


#Making main function
def main(data_file):
    #declaring stock variable and creating lists or dictionaries
    volume_list = []
    date_list = []
    open_value_list = []
    highest_value_list = []
    lowest_value_list = []
    close_value_list = []
    date_count_per_month = dict()

    # for loops to split the datas and appending it to respective lists
    for i in range(1,len(data_file)) :
        y_temp = data_file[i].strip("\n").split(",")
        volume_list.append(int(y_temp[6]))
        date_list.append(y_temp[0])
        open_value_list.append(float(y_temp[1]))
        highest_value_list.append(float(y_temp[2]))
        lowest_value_list.append(float(y_temp[3]))
        close_value_list.append(float(y_temp[4]))

    # splitting the dates into an easier format to iterate and storing it in a sublist
    for dates in range(len(date_list)):
        date_temp = date_list[dates].split("-")
        date_list.append(date_temp)

    # Deleting the original dates which has the harder format to iterate
    del date_list[:len(date_list)//2]

    #adding number of days in a month to a dictionary based on index in list
    for j in range(1,len(date_list)):
        if date_list[j][2] < date_list[j-1][2]:
            date_count_per_month[f"{date_list[j-1][0]}-{date_list[j-1][1]}"] = j-1
        elif j == len(date_list)-1 :
            date_count_per_month[f"{date_list[j][0]}-{date_list[j][1]}"] = j
        else :
            continue

    #counting the dates in each year and months in each year
    month_2020,month_2021,month_2022 = 0,0,0
    for k in date_count_per_month.keys():
        if "2020" in k:
            date_2020 = date_count_per_month[k]
            month_2020 += 1
        elif "2021" in k :
            date_2021 = date_count_per_month[k]
            month_2021 += 1
        else :
            date_2022 = date_count_per_month[k]
            month_2022 += 1
        
    #Calculations of max volume, min volume, lowest open, highest close
    max_volume_2020 = max(volume_list[:date_2020+1]) 
    max_volume_2021 = max(volume_list[date_2020+1:date_2021+1])

    min_volume_2020 = min(volume_list[:date_2020+1])
    min_volume_2021 = min(volume_list[date_2020+1:date_2021+1])
    
    low_open_2020 = min(open_value_list[:date_2020+1])
    low_open_2021 = min(open_value_list[date_2020+1:date_2021+1])

    high_close_2020 = max(close_value_list[:date_2020+1])
    high_close_2021 = max(close_value_list[date_2020+1:date_2021+1])


    #calculating monthly average and closing average and adding months to a new list
    monthly_avg = []
    closing_avg = []
    month_list = list(date_count_per_month.keys())
    index_temp = 0
    for i in date_count_per_month.values():
        monthly_avg.append(sum(volume_list[index_temp:i+1])/(i+1-index_temp))
        closing_avg.append(sum(close_value_list[index_temp:i+1])/(i+1-index_temp))
        index_temp = i+1

    
    #Output based on formats
    print("\t\tApple Stock Analysis 2020 and 2021")
    print("\t\t\t  2020\t\t  2021\t\t  Total")
    print("-"*70)
    print(f"Max Volume \t\t{max_volume_2020:,}\t{max_volume_2021:,}\t{max_volume_2020+max_volume_2021:,}")    
    print(f"Min Volume \t\t{min_volume_2020:,}\t{min_volume_2021:,}\t{min_volume_2020+min_volume_2021:,}")    
    print(f"Lowest Open \t\t{low_open_2020:,}\t\t{low_open_2021:,}\t{low_open_2020+low_open_2021:,}")    
    print(f"Highest Close \t\t{high_close_2020:,}\t{high_close_2021:,}\t{high_close_2020+high_close_2021:,}")
    print(f"Highest Monthly Average {max(monthly_avg[:month_2020]):,.0f}\t{max(monthly_avg[month_2020:month_2021+month_2020]):,.0f}\t{(max(monthly_avg[:month_2020]))+(max(monthly_avg[month_2020:month_2021+month_2020])):,.0f}")
    print(f"Lowest Monthly Average  {min(monthly_avg[:month_2020]):,.0f}\t{min(monthly_avg[month_2020:month_2021+month_2020]):,.0f}\t{(min(monthly_avg[:month_2020]))+(min(monthly_avg[month_2020:month_2021+month_2020])):,.0f}")
    print(f"Annual Average \t\t{sum(volume_list[:date_2020+1])/date_2020:,.0f}\t{sum(volume_list[date_2020+1:date_2021+1])/date_2021:,.0f}\t{(sum(volume_list[:date_2020+1])/date_2020)+(sum(volume_list[date_2020+1:date_2021+1])/date_2021):,.0f}")

    #writing output to file
    s = int(time.time())
    # Opening new file
    output_file = open(f"D:\Python\School\\report_{s}.txt","w") # No error handling is required because if file does not exist, will make a new one
    #Writing outputs into file
    output_file.write("\t\tApple Stock Analysis 2020 and 2021\n")
    output_file.write("\t\t\t\t\t\t  2020\t\t\t  2021\t\t\t Total\n")
    output_file.write(f"{'*'*70}\n")
    output_file.write(f"Max Volume\t\t\t\t{max_volume_2020:,}\t\t{max_volume_2021:,}\t\t{max_volume_2020+max_volume_2021:,}\n")    
    output_file.write(f"Min Volume\t\t\t\t{min_volume_2020:,}\t\t{min_volume_2021:,}\t\t{min_volume_2020+min_volume_2021:,}\n")    
    output_file.write(f"Lowest Open\t\t\t\t{low_open_2020:,}\t\t\t{low_open_2021:,}\t\t{low_open_2020+low_open_2021:,}\n")    
    output_file.write(f"Highest Close\t\t\t{high_close_2020:,}\t\t{high_close_2021:,}\t\t{high_close_2020+high_close_2021:,}\n")
    output_file.write(f"Highest Monthly Average\t{max(monthly_avg[:month_2020]):,.0f}\t{max(monthly_avg[month_2020:month_2021+month_2020]):,.0f}\t{(max(monthly_avg[:month_2020]))+(max(monthly_avg[month_2020:month_2021+month_2020])):,.0f}\n")
    output_file.write(f"Lowest Monthly Average\t{min(monthly_avg[:month_2020]):,.0f}\t{min(monthly_avg[month_2020:month_2021+month_2020]):,.0f}\t{(min(monthly_avg[:month_2020]))+(min(monthly_avg[month_2020:month_2021+month_2020])):,.0f}\n")
    output_file.write(f"Annual Average\t\t\t{sum(volume_list[:date_2020+1])/date_2020:,.0f}\t{sum(volume_list[date_2020+1:date_2021+1])/date_2021:,.0f}\t{(sum(volume_list[:date_2020+1])/date_2020)+(sum(volume_list[date_2020+1:date_2021+1])/date_2021):,.0f}\n")
    output_file.close() #Closing the file to prevent unintentional edits

    #Asking for year input to display charts
    year_input = input("Please input the year you want to see [2020/2021/2022]: ")
    #Setting conditionals and error handling and calling each chart function
    if year_input == "2020":
        chart_2020(monthly_avg,month_2020,month_list,closing_avg)
    elif year_input == "2021":
        chart_2021(monthly_avg,month_2020,month_2021,month_list,closing_avg)
    elif year_input == "2022":
        chart_2022(monthly_avg,month_2020,month_2021,month_list,closing_avg)
    else:
        print("Wrong Input")


# Making Chart Functions and using matplotlib to display the charts
def chart_2020(monthly_avg,month_2020,month_list,closing_avg):
    #Monthly average vs Months Chart 2020
    plt.plot(month_list[:month_2020],monthly_avg[:month_2020])
    plt.title("Monthly Average of 2020")
    plt.xlabel("Month")
    plt.ylabel("Monthly Average (*10^8)")
    plt.show()

    #Closing average vs Months Chart 2020
    plt.plot(month_list[:month_2020],closing_avg[:month_2020])
    plt.title("Closing avg 2020")
    plt.xlabel("Month")
    plt.ylabel("Monthly Closing Average")
    plt.show()



def chart_2021(monthly_avg,month_2020,month_2021,month_list,closing_avg):
    #Monthly average vs Months 2021
    plt.plot(month_list[month_2020:month_2021+month_2020],monthly_avg[month_2020:month_2021+month_2020])
    plt.title("Monthly avg 2021")
    plt.xlabel("Month")
    plt.ylabel("Monthly Average (*10^8)")
    plt.show()

    #Closing average vs Months 2021
    plt.plot(month_list[month_2020:month_2021+month_2020],closing_avg[month_2020:month_2021+month_2020])
    plt.title("Closing avg 2021")
    plt.xlabel("Month")
    plt.ylabel("Monthly Closing Average")
    plt.show()

def chart_2022(monthly_avg,month_2020,month_2021,month_list,closing_avg):
    #Monthly average vs Months 2022
    plt.plot(month_list[month_2021+month_2020:],monthly_avg[month_2021+month_2020:])
    plt.title("Monthly avg 2022")
    plt.xlabel("Month")
    plt.ylabel("Monthly Average (*10^8)")
    plt.show()

    #Closing average vs Months 2022
    plt.plot(month_list[month_2021+month_2020:],closing_avg[month_2021+month_2020:])
    plt.title("Closing avg 2022")
    plt.xlabel("Month")
    plt.ylabel("Monthly Closing Average")
    plt.show()


#Using while loops and setting condition
while again.lower() == "y":
    main(file_open()) #Calling main function 

    again = input("Would you like to repeat/try again?[y/n]") #Updating the condition based on user input

else :
    print("Have a great day!") #End condition