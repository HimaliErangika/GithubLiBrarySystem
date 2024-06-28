import datetime
import os
#os.getcwd()

class LMS: 
    """ This class used keep  records of books library
    It has four module"""
    
    def __init__(self,list_of_books , library_name) :
        self.list_of_books ="C:\PythonExperiment\list_of_books.txt"  #give absolute path
        self.library_name ="Python Library"
        self.books_dict ={}
        Id=101
        with open(self.list_of_books) as bk:  #with statement is used in exception handling to make the code cleaner and much more readabl --
            content=bk.readlines()
        for line in content:
            #print(line)
            self.books_dict.update({str(Id):{"books_title":line.replace("\n" ,""),
                                             "lender_name":"","issue_date":"","Status":"Available"}})
            Id=Id +1
    
    def display_books(self):
        print("---------------List of  Books ------------------")
        print("Books Id", "\t" , "Title")
        print("------------------------------------------------") 
        
        for key,value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"- [" , value.get("Status"),"]")
            
    def Issue_books(self):
        books_id =input("Enter book ID: ")
        current_date =datetime.datetime.now().strftime("%M/%D/%Y, %H:%M:%S") 
          
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['Status']=="Available":
                print(f"This books is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['Issue_date']}")
                return self.Issue_books()
            elif self.books_dict[books_id]['Status']=="Available":
                your_name =input("Enter your name: ")
                self.books_dict[books_id]['lender_name']=your_name
                self.books_dict[books_id]['issue_date']= current_date 
                self.books_dict[books_id]['Status']= "Already Issued"
                print("Books Issued Successfully !!! \n")
        else:
            print("Books id is not found !!! \n")
            
            return self.Issue_books()
  #------------------------------------------end of issue books
  
  #---------module add_books
    def add_books(self):
        new_books =input("Enter books title: ")
        if new_books == "" :
            return self.add_books()
        elif len(new_books) > 30 :
            print("Books tiltle is too long , maximum characters is 30 ")
            return self.add_books()
        else:
            with open(self.list_of_books , "a") as bk:  
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':"",
                                                                         'Issue_date':"",'Status' : "Available"}})  
                print(f"This books '{new_books}' has been added successfullly !!!")
                
                
#-----------module return books 

    def ret_books(self):
        books_id =input("Enter book id :")  
        if books_id in self.books_dict.keys():
            if self.books.dict[books_id]['Status'] =="Available" :
                print("This books is already available , please check your book id")
                return self.ret_books() 
            elif not self.books_dict[books_id]['Status'] == "Available":
                self.books_dict[books_id]['lender_name'] =""  # make lender blank
                self.books_dict[books_id]['Issue_books'] ="" 
                self.books_dict[books_id]['Status'] ="Available"
                print("Successfully updated !!! \n")
                
            else:
                print("Books ID is not found")  
try:      
   myLMS = LMS("list_of_books.txt" , "Python Library")
         #LMS("list_of_books.txt","Python Library")
   press_key_list = {"D":"DSisplay Books","I":"Issue Books","A":"Add Books","R":"Return Books","Q":"Quit"}   
   
   key_press =False 
   while not (key_press =="q") :
          print(f"\n-------------------Welcome To{myLMS.library_name} Library Management System------ \n")
                    # shift + Tab  --> moving block to the right
          
          for key , value in press_key_list.items():
            print("press" ,key , "To" , value)
          key_press = input("Press key: ").lower()
          if key_press == "i" :
            print("\nCurrent Selection : Issue Books\n")
            myLMS.Issue_books()
          elif key_press == "a" :
            print("\nCurrent Selection : Add Books\n")
            myLMS.add_books()
          elif key_press == "r" :
            print("\nCurrent Selection : Return Books\n")
            myLMS.ret_books()  
          elif key_press == "d" :
            print("\nCurrent Selection : Display Books\n")
            myLMS.display_books()
          elif key_press == "q" :
            break
          else: 
            continue
            
except Exception as e:
        print("Something Went Wrong , Please Check your Input !!!") 