#COSC1519 Introduction to Programming
#Assessment 3 Programming Project
#Student name: Ethan Haberl
#Student number: s3842062
#Practical group Teacher: Steven Korevaar

def main():
    
    print(">> Welcome to store manager 2078 <<") #start up text as well as line below
    print("Loading data from file: A3_s3842062_stock.txt")
    copy_stock_data("A3_s3842062_stock.txt", "updated_A3_s3842062_stock.txt")
    looper = True #looper will stay true until user tries to save and exit, this keeps the program running
    while looper == True:  
        stock_names = read_stock_names("updated_A3_s3842062_stock.txt") #get all stock data in lists to start
        stock_price = read_stock_price("updated_A3_s3842062_stock.txt")
        stock_quantities = read_stock_quantity("updated_A3_s3842062_stock.txt")
        stock_category1 = read_stock_category1("updated_A3_s3842062_stock.txt")
        stock_category2 = read_stock_category2("updated_A3_s3842062_stock.txt")

        try:
            print(">> What would you like to do? <<") #list all options
            print("1 - Show one item information")
            print("2 - Show all stock information")
            print("3 - Add/Update item")
            print("4 - Remove Item")
            print("5 - Compute stock value")
            print("6 - Save data and exit")
            first_input = int(input("7 - Exit without saving\n"))
            
        except:
            print("Please enter an integer\n") #if an integer is not selected then it will not error and ask again

        if first_input == 1: #first input is for single stock
            one_item_info(stock_names) #call single stock function
        elif first_input == 2: #second input is for all stock details
            all_stock_info(stock_names) #call all stock function
        elif first_input == 3: #third input is add/update item
            add_update_item(stock_names, stock_price, stock_quantities, stock_category1, stock_category2) #call add_update_item function
        elif first_input == 4: #fourth input is remove an item
            remove_item(stock_names, stock_price, stock_quantities, stock_category1, stock_category2)
        elif first_input == 5: #fifth input is calculate stock
            calculate_stock(stock_price, stock_quantities)
        elif first_input == 6: #sixth input is save and exit
            copy_stock_data("updated_A3_s3842062_stock.txt", "A3_s3842062_stock.txt") #copies data back into original stock
            print("Data saved and exited with code 0")
            looper = False #looper is false and program will now finish
        elif first_input == 7: #seventh input is end without saving
            looper = False #just ends the program without doing anything
            print("Exited with code 0")
        else:
            print("Please enter a number between 1 and 7\n")

def copy_stock_data(original_filename, copied_filename): 
    og_f = open(original_filename, 'r') #iterates through each line and writes it to the new file
    copy_f = open(copied_filename, 'w')
    for line in og_f:
        copy_f.write(line)
    og_f.close()
    copy_f.close()



def read_stock_names(filename):
    f = open(filename, 'r') #opens file in read
    stock_data = [] #set up stockdata to be written to
    for line in f: #goes through every line in the file
        if line.startswith("NAME"): continue #if line starts with NAME will not do anything (specifically for the first line)
        line = line.strip() #removes some weird characters if any
        line_list = line.split(',') #splits all commas and insets into a list
        stock_data.append(line_list[0]) #inserts the first index into stock_data
    f.close() #close file
    return stock_data

def read_stock_price(filename):
    f = open(filename, 'r') #opens file in read
    stock_data = [] #set up stockdata to be written to
    for line in f: #goes through every line in the file
        if line.startswith("NAME"): continue #if line starts with NAME will not do anything (specifically for the first line)
        line = line.strip() #removes some weird characters if any
        line_list = line.split(',') #splits all commas and insets into a list
        stock_data.append(line_list[1]) #inserts the first index into stock_data
    f.close() #close file
    return stock_data

def read_stock_quantity(filename):
    f = open(filename, 'r') #opens file in read
    stock_data = [] #set up stockdata to be written to
    for line in f: #goes through every line in the file
        if line.startswith("NAME"): continue #if line starts with NAME will not do anything (specifically for the first line)
        line = line.strip() #removes some weird characters if any
        line_list = line.split(',') #splits all commas and insets into a list
        stock_data.append(line_list[2]) #inserts the first index into stock_data
    f.close() #close file
    return stock_data

def read_stock_category1(filename):
    f = open(filename, 'r') #opens file in read
    stock_data = [] #set up stockdata to be written to
    for line in f: #goes through every line in the file
        if line.startswith("NAME"): continue #if line starts with NAME will not do anything (specifically for the first line)
        line = line.strip() #removes some weird characters if any
        line_list = line.split(',') #splits all commas and insets into a list
        stock_data.append(line_list[3]) #inserts the first index into stock_data
    f.close() #close file
    return stock_data

def read_stock_category2(filename):
    f = open(filename, 'r') #opens file in read
    stock_data = [] #set up stockdata to be written to
    for line in f: #goes through every line in the file
        if line.startswith("NAME"): continue #if line starts with NAME will not do anything (specifically for the first line)
        line = line.strip() #removes some weird characters if any
        line_list = line.split(',') #splits all commas and insets into a list
        stock_data.append(line_list[4]) #inserts the first index into stock_data
    f.close() #close file
    return stock_data



def read_stock_line(filename, linecount):
    f = open(filename, 'r') #open file in read
    counter = 0 #counter used in loop to loop until desired line
    item_data = []
    for line in f: #goes through every line in file
        if line.startswith("NAME"): continue #if line starts with NAME will not do anything (specifically for the first line)
        if counter == linecount: #only executes code if the counter is the same line as linecount
            line = line.strip() #removes some weird characters if any
            item_data = line.split(',') #splits all commas and insets into a list
        counter += 1 #increments counter
    f.close() #close file
    return item_data



def one_item_info(stock_names):
    print("Show one item information selected")
    item_name = input("What is the name of the item? ") #ask for name
    try:
        item_line = stock_names.index(item_name) #finds the index of the item in item_name to know what line it is
        item_data = read_stock_line("updated_A3_s3842062_stock.txt", item_line) #calls read_stock_line function to get the data in a list
        for data in item_data: #prints the data on a line seperated by spaces
            print(data, end=" ")
        print("")
    except: #if the item is not in the txt file returns an error message
        print("Error: item name \"", item_name, "\" not found!", sep="")


def all_stock_info(stock_names):
    print("Show all stock information selected")
    print("Showing all item information (by name alphabetical order)")
    print("NAME PRICE QUANTITY CATEGORY1[YOUNG'S MODULUS] CATEGORY2[YIELD STRENGTH]")
    sorted_stock_names = stock_names[:] #copies the stock names into another list to be sorted
    sorted_stock_names.sort() #sorts it alphabetically
    for j in range(0, len(stock_names)): #runs through every line in stock_names
        item_line = stock_names.index(sorted_stock_names[j])
        item_data = read_stock_line("updated_A3_s3842062_stock.txt", item_line) #calls read_stock_line function to get the data in a list
        for data in item_data: #prints the data on a line seperated by spaces
            print(data, end=" ")
        print("")
    

def add_update_item(stock_names, stock_price, stock_quantities, stock_category1, stock_category2):

    update_name = input("What is the name of the item you would like to add/update? ") #get the name to update
    if update_name in stock_names: #if the item is already in database
        print("Item already exists!") 
        item_line = stock_names.index(update_name) #finds the index of the item in item_name to know what line it is
        item_data = read_stock_line("updated_A3_s3842062_stock.txt", item_line) #calls read_stock_line function to get the data in a list
        for data in item_data: #prints current data for the item that will be changed for the user to reference
            print(data, end=" ")
        print("")
        new_item_dict = {}
        new_item_dict["name"] = update_name #adds name into dictionary under name
        print("Input new values:") #gets the new values and appends them to the new item data list
        while True: #in a loop to make sure the value entered is correct if not a float will ask again
            try:
                item_price = float(input("What is the (new) price? "))
                new_item_dict["price"] = str(item_price)
                break
            except:
                print("Please enter a number")
        while True:
            try:
                item_quantity = int(input("What is the (new) quantity? "))
                new_item_dict["quantity"] = str(item_quantity)
                break
            except:
                print("Please enter an integer")
        new_item_dict["category1"] = input("What is the (new) category1? ")
        new_item_dict["category2"] = input("What is the (new) category2? ")
        

        stock_price[item_line] = new_item_dict["price"] #stores the values gotten from the user in the same location that the name is stored in
        stock_quantities[item_line] = new_item_dict["quantity"] #this way it will be known that it is on the same line
        stock_category1[item_line] = new_item_dict["category1"]
        stock_category2[item_line] = new_item_dict["category2"]
        write_to_file("updated_A3_s3842062_stock.txt", stock_names, stock_price, stock_quantities, stock_category1, stock_category2) #call write to file function
        print("Update successful!")
        for data in new_item_dict: #prints the new data that the user input
            print(new_item_dict[data], end=" ")
        print("")

    else: #if the new item is not in the database
        print("Item is new")
        new_item_data = [] #set up list to store new data that the user will input
        new_item_data.append(update_name) #gets the new values and appends them to the new item data list 
        while True:
            try: #in a loop to make sure the value entered is correct if not a float will ask again
                item_price = float(input("What is the (new) price? "))
                new_item_data.append(str(item_price))
                break
            except:
                print("Please enter a number")
        while True:
            try:
                item_quantity = int(input("What is the (new) quantity? "))
                new_item_data.append(str(item_quantity))
                break
            except:
                print("Please enter an integer")
        new_item_data.append(input("What is the (new) category1? "))
        new_item_data.append(input("What is the (new) category2? "))
        append_to_file("updated_A3_s3842062_stock.txt", new_item_data) #calls appends to file function
        for data in new_item_data: #displays the new item that the user has input
            print(data, end=" ")
        print("")


def append_to_file(filename, line_data):
    f = open(filename, 'a') #opens file in append mode
    #concatenates the new data to string with commas seperating them
    s = line_data[0] + "," + line_data[1] + "," + line_data[2] + "," + line_data[3] + "," + line_data[4] + "\n" 
    f.write(s) #appends concatenated data to file
    f.close()

def write_to_file(filename, stock_names, stock_price, stock_quantities, stock_category1, stock_category2):
    f = open(filename, 'w') #opens file in write mode
    f.write("NAME,PRICE,QUANTITY,CATEGORY1,CATEGORY2\n") #writes the headings first
    for index in range(0, len(stock_names)): #for each name stored in stock_names
        #concatenates all the data sent to function into a string
        s = stock_names[index] + "," + stock_price[index] + "," + stock_quantities[index] + "," + stock_category1[index] + "," + stock_category2[index] + "\n"
        f.write(s) #writes string to file
    f.close()

def remove_item(stock_names, stock_price, stock_quantities, stock_category1, stock_category2):
    item_name = input("What is the name of the item you would like to remove? ")
    if item_name in stock_names: #only does the code if the item actually exists
        item_line = stock_names.index(item_name) #finds the index of the item in item_name to know what line it is
        del(stock_names[item_line]) #deletes all the data from that index in each category and then writes to the updated stock file
        del(stock_price[item_line])
        del(stock_quantities[item_line])
        del(stock_category1[item_line])
        del(stock_category2[item_line])
        write_to_file("updated_A3_s3842062_stock.txt", stock_names, stock_price, stock_quantities, stock_category1, stock_category2) #call write to file function
        print(item_name, "removed")
    else:
        print("That item is not in the stock!")

def calculate_stock(stock_price, stock_quantities):
    total_stock = 0.0 #initialise stock variable
    for i in range(0, len(stock_price)): #goes through every item in the system
        total_stock += (float(stock_price[i]) * float(stock_quantities[i])) #multiplies the price by the quantity and adds to the total
    print("The total stock value is:", total_stock)


main()
