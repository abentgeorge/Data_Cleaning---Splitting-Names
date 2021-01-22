import pandas as pd


excel_workbook = 'toclean.xlsx'


sheet1 = pd.read_excel(excel_workbook)

print(sheet1.head(10))


##         TASK 1) CREATE SEPERATE LISTS(COLUMNS) FOR FIRST NAME AND LAST NAME

first_name_list =[]

last_name_list =[]


# FOR LOOP - FOR EVERY ENTRY SEPERATE FIRST NAME AND LAST NAME AND ADD TO LISTS:
#             pull out the column into a df first

excel_names = sheet1['first_name']

#  print(excel_names)

for name in excel_names:
    
    first_name, last_name = name.split(' ', 1)  #.split = splits based on space b/w
    
    # Append into lists  Use .upper to change to uppercase
    
    first_name_list.append(first_name)
    
    last_name_list.append(last_name)
    
print(first_name_list)

print(sheet1.head())

######  ADDING seperation BACK INTO DATAFRAME

sheet1.insert(0, "first", first_name_list)  # .insert( 0th position, column name, list to extract from)
sheet1.insert(1, "last", last_name_list)


# DELETE THE ORIGINAL JOINED COLUMN

del sheet1['first_name']

print(sheet1.head())

sheet1.to_excel("cleandummyoutput.xlsx")