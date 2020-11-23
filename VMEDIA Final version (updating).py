#IMPORTS
from tkinter import * #tkinter will be used to create my GUI
from tkinter import font, messagebox
import hashlib

from datetime import datetime, timedelta, date #These were the modules I needed to be able to update the users watch time data
import time#^^

#Matplotlib is used to create and display graphs of viewing time against time
import matplotlib.pyplot as plt
import matplotlib.ticker as plttick


#Instantiating the root window
root = Tk() #Creates the root window
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight())) #Creates a full screen window
root.title("VMedia") #Sets the name of the window
#root.overrideredirect(True)

SALT ="T1xR3Pk98N" #Salt value that gets added to the users password
                
class HyperlinkManager:
    #Sets up the HyperlinkManager class
    def __init__(self, text, menu_title, list_of_films, scroll_bar, colour_schemes_button, user_details, user_film_choices, film_list, login_username_encrypted
                 , back_col, fore_col, button_col, scheme, watched_time_list, sign_out_button, search_entry, revert_button,
                filter_heading_label, disney_label, disney_button, action_label, action_button,
                adventure_label, adventure_button, comedy_label, comedy_button, romance_label,
                romance_button, horror_label, horror_button, dc_label, dc_button,
                 chick_flicks_label, chick_flicks_button, sci_fi_label, sci_fi_button,
                musicals_label, musicals_button, classics_label, classics_button,
                thriller_label, thriller_button, fantasy_label, fantasy_button,
                marvel_label, marvel_button, graph_button, submit_filters, search_button):
        
        self.text = text
        self.text.tag_config("hyper")
        self.text.tag_bind("hyper", "<Enter>", self._enter) #When the cursor enters the text box call the class function _enter
        self.text.tag_bind("hyper", "<Leave>", self._leave) #When the cursor leaves the text box call the class function _leave
        self.text.tag_bind("hyper", "<Button-1>", lambda eff: self._click("<Button-1>",menu_title, list_of_films,
                                                                          scroll_bar, colour_schemes_button, user_details, user_film_choices, film_list, login_username_encrypted
                                                                          , back_col, fore_col, button_col, scheme, watched_time_list,
                                                                          sign_out_button, search_entry, revert_button,
                                                                           filter_heading_label, disney_label, disney_button, action_label, action_button,
                                                                           adventure_label, adventure_button, comedy_label, comedy_button, romance_label,
                                                                           romance_button, horror_label, horror_button, dc_label, dc_button,
                                                                          chick_flicks_label, chick_flicks_button, sci_fi_label, sci_fi_button,
                                                                          musicals_label, musicals_button, classics_label, classics_button,
                                                                           thriller_label, thriller_button, fantasy_label, fantasy_button,
                                                                           marvel_label, marvel_button, graph_button, submit_filters, search_button))
                                                                          #When the user clicks on a link go to the class function _click
        self.reset() #Calls the class function called reset

    #This class function resets the list of films to being empty
    #Because of this when the search button is pressed again the values dont exceed the length of possible_searches
    def reset(self):
        self.links = {}


    #Adds an action to perforemed when the line is clicked.
    #returns the tags to be used in the associated text widget
    def add(self, action):
        tag = "hyper-%d" % len(self.links)
        self.links[tag] = action
        return "hyper", tag

    #When the users cursor enters the text contained within the text box
    #Turn the users cursor to hand2
    def _enter(self, event):
        self.text.config(cursor="hand2")

    #When the users cursor leaves the text contained within the text box
    #Turn the users cursor back to normal
    def _leave(self, event):
        self.text.config(cursor="")

    #When the user clicks on one of the lines in the text box


           
    def _click(self, reference_number,menu_title, list_of_films, scroll_bar, colour_schemes_button, user_details, user_film_choices, film_list, login_username_encrypted,
           back_col, fore_col, button_col, scheme, watched_time_list,
           sign_out_button, search_entry, revert_button,
           filter_heading_label, disney_label, disney_button, action_label, action_button,
           adventure_label, adventure_button, comedy_label, comedy_button, romance_label,
           romance_button, horror_label, horror_button, dc_label, dc_button,
           chick_flicks_label, chick_flicks_button, sci_fi_label, sci_fi_button,
           musicals_label, musicals_button, classics_label, classics_button,
           thriller_label, thriller_button, fantasy_label, fantasy_button,
           marvel_label, marvel_button, graph_button, submit_filters, search_button):
        
        for tag in self.text.tag_names(CURRENT):
            reference_number = tag[6:] #Gets the line of the text file (which will will be the same as the index of the list)
            if tag[:6] == "hyper-": #If the first six characters of that lines tag are hyper- then,
                self.links[tag](reference_number,menu_title, list_of_films, scroll_bar, colour_schemes_button, user_details, user_film_choices, film_list, login_username_encrypted,
           back_col, fore_col, button_col, scheme, watched_time_list,
           sign_out_button, search_entry, revert_button,
           filter_heading_label, disney_label, disney_button, action_label, action_button,
           adventure_label, adventure_button, comedy_label, comedy_button, romance_label,
           romance_button, horror_label, horror_button, dc_label, dc_button,
           chick_flicks_label, chick_flicks_button, sci_fi_label, sci_fi_button,
           musicals_label, musicals_button, classics_label, classics_button,
           thriller_label, thriller_button, fantasy_label, fantasy_button,
           marvel_label, marvel_button, graph_button, submit_filters, search_button) #activate that lines command

def just_close(event = None, text = "Do you want to quit?"): #A function designed to close the system
    if messagebox.askyesno("Quit", text): #Displays a message to make sure the user wants to quit
        quit()#A method that kills the program


def closed_update(user_details=None, user_film_choices=None, login_username_encrypted=None, scheme=None, watched_time_list=None, event = None, text = "Do you want to quit?"): #A function designed to close the system
    print(watched_time_list)
    if messagebox.askyesno("Quit", text): #Displays a message to make sure the user wants to quit
        new_user_data = "" #This is the variable that will eventually contain all of the users new details


        if scheme == "default":
            user_details[3]="default"
            
        elif scheme == "monochrome":
            user_details[3]="monochrome"

        elif scheme == "matrix":
            user_details[3]="matrix"

        elif scheme == "colour splash":
            user_details[3]="colour splash"

        elif scheme == "default":
            user_details[3]="default"

        elif scheme == "toxic":
            user_details[3]="toxic"

            
        for finalised_user_details in range(len(user_details)):
            if finalised_user_details == len(user_details)-1:
                new_user_data = new_user_data + user_details[finalised_user_details].strip() + "/"
            else:
                new_user_data = new_user_data + user_details[finalised_user_details].strip() + ","

        #Format watched_time_list    
        for finalised_watched_time in range(len(watched_time_list)):
            stored_time_value, stored_time_date = str((watched_time_list[finalised_watched_time]).strip()).split(" ")
            if finalised_watched_time == len(watched_time_list)-1:
                new_user_data = new_user_data + stored_time_value + "," + stored_time_date + "/"
            else:
                new_user_data = new_user_data + stored_time_value + "," + stored_time_date + ","

        #THIS LIMITS THE AMOUNT OF DATA THAT CAN BE STORED ON A USERS ACCOUNT TO THE 200 MOST RECENT ELEMENTS. THIS IS TO MAKE THE SUGGESTIONS RELEVANT AND UP TO DATE
        while len(user_film_choices)>200:
            del user_film_choices[0]

        for finalised_user_film_choices in range(len(user_film_choices)):
            if finalised_user_film_choices == len(user_film_choices)-1:
                new_user_data = new_user_data + user_film_choices[finalised_user_film_choices].strip()
            else:
                new_user_data = new_user_data + user_film_choices[finalised_user_film_choices].strip() + ","

        #Rewrites the users details in the new, correct, form        
        with open("accounts.txt", "r+") as accounts: #Opens the file so it can be read from and written to and also be ready to close it self
            all_data = [line.strip() for line in accounts] #Gets the data from all lines in the accounts text file
            for user in range(len(all_data)): #Gets each users data line by line
                user_data = all_data[user].split(",") #Users data gets set into individual items
                if user_data[0] == login_username_encrypted: #Reads the first item of all lines in the accounts text file
                    del all_data[user] #Removes the data that is currently stored for the user
                    accounts.truncate(0) #Clears the accounts file
                    accounts.seek(0,0) #Sets the pointer to the beginning of the file
                    for all_users in range(len(all_data)): #For each line in the accounts text file
                        accounts.write(all_data[all_users]+"\n") #Rewrite the line and start a new one
                    accounts.seek(0,2)#Sets the pointer to the end of the file
                    accounts.write(new_user_data + "\n") #Writes the updated users data
                    break #end for loop
                else:
                    pass #Increment user by one
                
        quit()#A method that kills the program


        

def show_change(element, button):
    if element["show"] == "*": #If password is already displaying *
        element["show"] = "" #Display normal text
        button["bg"] = "black" #And make the relevant button black
        
    else: #Otherwise
        element["show"] = "*" #Display *
        button["bg"] = "white" #And make the relevant button white
        
def underline(label): #A reusable function where a label is passed in so it can be underlined
    f = font.Font(label, label.cget("font"))#Creates a new font
    f.configure(underline=True) #Underlines the new font
    label.configure(font=f) #Applies the new underlined font to the label

def colour_toggle(current_back_col):
    if current_back_col == "steelblue":
        back_col="black"
        fore_col="white"
        button_col="white"
        toggled_mode = "on"
    else:
        back_col="steelblue"
        fore_col="lightgoldenrod1"
        button_col="pink"
        toggled_mode = "off"
        
    opening(back_col, fore_col, button_col, toggled_mode)

def colour_change(user_details, user_film_choices, film_list, login_username_encrypted,back,fore,button_colour,text,
                  button1,button2,button3, button4, button5, button6, scheme, scheme_determination, home_button, watched_time_list, home=None):
    print(home_button)
    text.destroy()#Destorys the colour schemes heading
    #Destroys all the colour scheme buttons
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    home_button.destroy()

    if home: #If the home button was pressed
        main(user_details, user_film_choices, film_list, login_username_encrypted, back, fore, button_colour, scheme, watched_time_list) #Go to the main funcion
        
    else: #Otherwise
        #Update all colours
        back_col = back
        fore_col = fore
        button_col = button_colour
        root.config(bg = back_col)

        if scheme_determination == "monochrome":
            scheme = "monochrome"

        elif scheme_determination == "posh":
            scheme = "posh"

        elif scheme_determination == "matrix":
            scheme = "matrix"

        elif scheme_determination == "colour splash":
            scheme = "colour splash"

        elif scheme_determination == "default":
            scheme = "default"

        elif scheme_determination == "toxic":
            scheme = "toxic"

        colour_schemes(user_details, user_film_choices, film_list, login_username_encrypted,back_col,fore_col,button_col, scheme, watched_time_list)
        
def colour_schemes(user_details, user_film_choices, film_list, login_username_encrypted,back_col,fore_col,button_col, scheme, watched_time_list):
    #Creates a heading and underlines it
    colours_heading = Label(root,text = "Colour Schemes", font=("arial",50,"bold"), fg=fore_col, bg=back_col)
    colours_heading.pack(side = "top")
    underline(colours_heading)
    
    #Create the colour scheme buttons
    scheme1 = Button(root, text="Monochrome", font=("arial",10,"bold"),bg=button_col, command = lambda: colour_change(user_details, user_film_choices, film_list,
                    login_username_encrypted,"black","white","white", colours_heading, scheme1, scheme2, scheme3, scheme4, scheme5, scheme6, scheme, "monochrome", home, watched_time_list), relief=GROOVE, bd=6)
    scheme1.place(relx=0.25,rely=0.35,relwidth = 0.2, relheight = 0.2, anchor = "center")

    scheme2 = Button(root, text="Posh", font=("arial",10,"bold"), bg=button_col, command = lambda: colour_change(user_details, user_film_choices, film_list,
                    login_username_encrypted,"snow","lightgoldenrod1","lightgoldenrod1", colours_heading, scheme1, scheme2, scheme3, scheme4, scheme5, scheme6, scheme, "posh", home, watched_time_list), relief=GROOVE, bd=6)
    scheme2.place(relx=0.50, rely=0.35, relwidth = 0.2, relheight = 0.2, anchor = "center")

    scheme3 = Button(root, text="matrix", font=("arial",10,"bold"), bg=button_col, command = lambda: colour_change(user_details, user_film_choices, film_list,
                    login_username_encrypted,"black","lime","lime", colours_heading, scheme1, scheme2, scheme3, scheme4, scheme5, scheme6, scheme, "matrix", home, watched_time_list), relief=GROOVE, bd=6)
    scheme3.place(relx=0.75, rely=0.35, relwidth = 0.2, relheight = 0.2, anchor = "center")

    scheme4 = Button(root, text="Colour Splash", font=("arial",10,"bold"), bg=button_col, command = lambda: colour_change(user_details, user_film_choices, film_list,
                    login_username_encrypted,"yellow","blue","red", colours_heading, scheme1, scheme2, scheme3, scheme4, scheme5, scheme6, scheme, "colour splash", home, watched_time_list), relief=GROOVE, bd=6)
    scheme4.place(relx=0.25, rely=0.60, relwidth = 0.2, relheight = 0.2, anchor = "center")

    scheme5 = Button(root, text="Default", font=("arial",10,"bold"), bg=button_col, command = lambda: colour_change(user_details, user_film_choices, film_list,
                    login_username_encrypted,"steelblue","lightgoldenrod1","pink", colours_heading, scheme1, scheme2, scheme3, scheme4, scheme5, scheme6, scheme, "default", home, watched_time_list), relief=GROOVE, bd=6)
    scheme5.place(relx=0.50, rely=0.60, relwidth = 0.2, relheight = 0.2, anchor = "center")

    scheme6 = Button(root, text="Toxic", font=("arial",10,"bold"), bg=button_col, command = lambda: colour_change(user_details, user_film_choices, film_list,
                    login_username_encrypted,"green","yellow","lime", colours_heading, scheme1, scheme2, scheme3, scheme4, scheme5, scheme6, scheme, "toxic", home, watched_time_list), relief=GROOVE, bd=6)
    scheme6.place(relx=0.75, rely=0.60, relwidth = 0.2, relheight = 0.2, anchor = "center")

    #Create the home button
    home = Button(root, text="home", font=("arial",10,"bold"), bg=button_col, command = lambda: colour_change(user_details, user_film_choices, film_list, login_username_encrypted,
                            back_col, fore_col, button_col, colours_heading, scheme1, scheme2, scheme3, scheme4, scheme5, scheme6, scheme, "home_pressed", home, watched_time_list, True), relief=GROOVE, bd=6)
    home.place(relx=0.50, rely=0.90, relwidth = 0.8, relheight = 0.1, anchor = "center")

def opening(back_col = "steelblue", fore_col = "lightgoldenrod1", button_col = "pink", toggled_mode="off"): #The first function in my system, you can pick whether you would like to login or signup
    root.bind('<Escape>',just_close) #Binds the escape key to the function named closed
    root.protocol("WM_DELETE_WINDOW", just_close) #When the window is attempted to be closed go to the close function
    root.config(bg = back_col) #Sets the background colour of the root window

    current_back_col = back_col

    #Label for title
    welcoming = Label(root,text = "Welcome to VMedia", font=("arial",50,"bold"), fg=fore_col, bg=back_col) #Creates a label welcoming the user to VMedia
    welcoming.pack(side = "top") #Outputs the label at the top of the window
    underline(welcoming)

    #Login button
    login_button = Button(root, text="Login", font=("arial",10,"bold"),bg=button_col, command = lambda: welcoming.destroy() or login_button.destroy() or signup_button.destroy()
                           or text.destroy() or colour_blindness_button.destroy() or login(back_col, fore_col, button_col), relief=GROOVE, bd=6)
    #Displays the button that takes you to the login function ^
    login_button.place(relx=0.35,rely=0.45,relwidth = 0.25, relheight = 0.2, anchor = "center") #Places the button exactly where i want it in relation to the size of the root window and centralises it

    #Signup button
    signup_button = Button(root, text="Signup", font=("arial",10,"bold"), bg=button_col, command = lambda: welcoming.destroy() or login_button.destroy() or signup_button.destroy()
                           or text.destroy() or colour_blindness_button.destroy() or signup(back_col, fore_col, button_col), relief=GROOVE, bd=6)
    #Displays the button that takes you to the signup function ^
    signup_button.place(relx=0.65, rely=0.45, relwidth = 0.25, relheight = 0.2, anchor = "center") #Places the button exactly where i want it in relation to the size of the root window and centralises it

    #Colour blindness button
    colour_blindness_button = Button(root, text="colour blindness mode: {}".format(toggled_mode), font=("arial",12,"bold"), bg=button_col, command = lambda:
                                   welcoming.destroy() or login_button.destroy() or signup_button.destroy()
                                   or text.destroy() or colour_blindness_button.destroy() or colour_toggle(current_back_col), relief=GROOVE, bd=6)
    colour_blindness_button.place(relx=0.85, rely=0.06, relwidth = 0.17, relheight = 0.1, anchor = "center") #Places the button exactly where i want it in relation to the size of the root window and centralises it
    
    #Text box
    text = Text(root,wrap=WORD,cursor = "arrow",bd=8, relief=GROOVE, font=("arial",20)) #Creates a text box
    text.tag_configure("bold", font="arial 20 bold")
    text.insert(INSERT, "VMedia is a piece of software designed to display a variety of films and tv shows you would like to watch. You can filter\
 suggestion to better suit you by removing films and tv shows from a certain genre. Films can be searched for individually if you wish and the films you\
   watch will be logged automaticaly to help the AI suggest films you like more accurately as you begin to use VMedia more. This helps create an experience\
 that's custom made to your taste.") #Inserts text into the text box

    text.insert("end", " To close VMedia press the escape key", "bold")
    text.place(relx=0.105, rely=0.6, relwidth = 0.8, relheight = 0.3) #Displays the text box to the user
    text.config(state="disabled") #Stops the user from being able to write into the text box

def signup(back_col, fore_col, button_col):
    #MAIN LABEL
    sign_up_label = Label(root, text="Please Signup", font=("arial",30,"bold"),fg=fore_col, bg=back_col)
    sign_up_label.place(relx = 0.05, rely = 0.05) #Places the label on screen
    underline(sign_up_label)

    #Labels for text boxes
    username_label = Label(root, text="Username:", font=("arial",15,"bold"),fg=fore_col, bg=back_col)
    username_label.place(relx = 0.05, rely = 0.25) #Places the label on screen

    password_label = Label(root, text="Password:", font=("arial",15,"bold"),fg=fore_col, bg=back_col)
    password_label.place(relx = 0.05, rely = 0.35) #Places the label on screen

    check_label = Label(root, text="Re-enter password:", font=("arial",15,"bold"),fg=fore_col, bg=back_col)
    check_label.place(relx = 0.05, rely = 0.45) #Places the label on screen

    email_label = Label(root, text="Email:", font=("arial",15,"bold"),fg=fore_col, bg=back_col)
    email_label.place(relx = 0.05, rely = 0.55) #Places the label on screen

    #ENTRY BOXES
    signup_username_entry = Entry(root,relief=GROOVE, bd=2, font=("arial",13)) #Creates a text entry box
    
    signup_password_entry = Entry(root,relief=GROOVE, bd=2, font=("arial",13), show = "*") # ^^
    
    check_password_entry = Entry(root,relief=GROOVE, bd=2, font=("arial",13), show = "*") # ^^
    
    email_entry = Entry(root,relief=GROOVE, bd=2, font=("arial",13)) # ^^

    #Change the password entry fields to show normal text
    change_password_format = Button(text = "", bg = "white", relief=GROOVE, bd=6, command = lambda:
                                    show_change(signup_password_entry, change_password_format) or show_change(check_password_entry, change_password_format))
    change_password_format.place(relx=0.41,rely=0.35,relwidth=0.025, relheight=0.15)
    
    #PLACE ENTRY BOXES
    signup_username_entry.place(relx = 0.20, rely = 0.25, relwidth = 0.2, relheight = 0.05) #Places the text entry box on screen
    signup_password_entry.place(relx = 0.20, rely = 0.35, relwidth = 0.2, relheight = 0.05) #^^
    check_password_entry.place(relx = 0.20, rely = 0.45, relwidth = 0.2, relheight = 0.05) #^^
    email_entry.place(relx = 0.20, rely = 0.55, relwidth = 0.2, relheight = 0.05) #^^

    #ERROR MESSAGE FOR SIGNUP_USERNAME
    username_error = Label(root, text = "Username must be at least 7 characters long", font=("arial",12, "bold"), fg = "red", bg=back_col)

    #ERROR MESSAGE FOR SIGNUP_PASSWORD
    password_length_error = Label(root, text = "Password must be a minimum of 10 characters long", font=("arial",12, "bold"), fg = "red", bg=back_col)

    #ERROR MESSAGE FOR CHECK_PASSWORD
    password_contents_error = Label(root, text = "Password must contain at least one capital letter and number", font=("arial",12, "bold"), fg = "red", bg=back_col)

    #ERROR MESSAGE FOR EMAIL
    email_error = Label(root, text = "Email not found", font=("arial",12, "bold"),fg = "red", bg=back_col)

    #ERROR MESSAGE DISPLAYED WHEN PASSWORDS DONT MATCH
    match_error = Label(root, text = "Passwords don't match", font=("arial",15, "bold"),fg = "red", bg=back_col)

    #ERROR MESSAGE DISPLAYED WHEN USERNAME IS TAKEN
    taken_error = Label(root, text = "Username is already taken", font=("arial",15, "bold"),fg = "red", bg=back_col)

    #HOME BUTTON
    home_signup = Button(root, text = "Home", font=("arial",15,"bold"), command = lambda: signup_clear(home_signup, signup_username_entry, signup_password_entry, check_password_entry, email_entry, change_password_format,
                                   username_error, password_length_error, password_contents_error, email_error, match_error, taken_error,
                                   sign_up_label, username_label, password_label, check_label, email_label, submit, back_col, fore_col, button_col),
                         bg=button_col, relief=GROOVE, bd=6)
    home_signup.place(relx = 0.80, rely = 0.05, relwidth = 0.15, relheight = 0.1)
    
    #SUBMIT BUTTON
    submit = Button(root, text = "Submit details", font=("arial",15,"bold"), command = lambda:
                    check_contents(home_signup, signup_username_entry, signup_password_entry, check_password_entry, email_entry, change_password_format,
                                   username_error, password_length_error, password_contents_error, email_error, match_error, taken_error,
                                   sign_up_label, username_label, password_label, check_label, email_label, submit, back_col, fore_col, button_col),
                    bg=button_col, relief=GROOVE, bd=6)

    submit.place(relx = 0.05, rely = 0.85, relwidth = 0.3, relheight = 0.1) #Places the submit button on screen.


def check_contents(home_signup, signup_username_entry, signup_password_entry, check_password_entry, email_entry, change_password_format,
                   username_error, password_length_error, password_contents_error, email_error, match_error, taken_error,
                   sign_up_label, username_label, password_label, check_label, email_label, submit, back_col, fore_col, button_col): #The function that will be used to check the contents of signup_password

    signup_password = signup_password_entry.get() #Retrieves the data stored in signup_password_entry
    signup_username = signup_username_entry.get() #Retrieves the data stored in signup_username_entry
    check_password = check_password_entry.get()
    email = email_entry.get()#Retrieves the data stored in check_password_entry

    #Boolean values used to output message to user  
    digit_val = 1 #Password digit test
    length_val = 1 #Password length test
    caps_val = 1 #Password capital letter test
    name_val = 1 #Username length test
    email_val = 1 #Email validation test
    taken = 0 #Username taken test
    
    #Username Validation
    if len(signup_username) >=7: #Checks to see if the users username is 7 or more characters long
        username_error.place_forget() #Hide the caps_error label
        name_val = 0 #Signifies that the test was passed
    else:
        username_error.place(relx = 0.41, rely = 0.255)
        #Makes the relevent error message visible

    #Email Validation
    if len(email) == 0:
        email_error.place(relx = 0.41, rely = 0.555)
    else:
        for character in range(len(email)): #For length of email
            if email[character] == "@" and email[len(email)-4:] == ".com": #Checks if email has a @ symbol in and it and if the last 4 characters are .com
                email_val = 0 #Signifies that the test was passed
                email_error.place_forget()
                break
            else:
                email_error.place(relx = 0.41, rely = 0.555)
            
    #Password Validation  
    if len(signup_password) >= 10: #Checks to see if the users password is 10 or more character long
        length_val = 0 #Signifies that the test was passed
        password_length_error.place_forget()
    else:
        password_length_error.place(relx = 0.46, rely = 0.455)
                        

    if len(signup_password) == 0:
        password_contents_error.place(relx = 0.46, rely = 0.355)
    else:                 
        for index in range(len(signup_password)): #For length of password
            if signup_password[index].isdigit(): #Checks each individual character to see if its a number
                digit_val = 0 #Signifies that the test was passed
            if signup_password[index].isupper(): #Checks each individual character to see if its a number
                caps_val = 0 #Signifies that the test was passed
            if digit_val == 0 and caps_val==0:
                password_contents_error.place_forget()
                break #Ends current for loop
            else:
                password_contents_error.place(relx = 0.46, rely = 0.355)

    #Checking that passwords match
    if signup_password == check_password: #If passwords are the same
        match_error.place_forget()
    else:
        match_error.place(relx = 0.05, rely = 0.65)

    #Checks if a users username is already taken
    #Uses try so that if the accounts file doesn't exist on the users device the system doesn't break
    #Encrypt the users username          
    hashing_username= hashlib.sha256((signup_username+SALT).encode()) #Hashes signup_username
    hashed_username = hashing_username.hexdigest() #^^
    try:
        with open("accounts.txt", "r") as accounts: #Opens the file read only and ready to close it self
            all_data = [line.strip() for line in accounts] #Gets the data from all lines in the accounts text file
            for user in range(len(all_data)): #Gets each users data line by line
                user_data = all_data[user].split(",") #Users data gets set into individual items
                if user_data[0] == hashed_username: #Reads the first item of all lines in the accounts text file
                    taken = 1 #Signifies the test was failed
                    taken_error.place(relx = 0.05, rely = 0.75)
                    break
                else:
                    taken_error.place_forget()
    except:
        pass
    
    #OUTCOME TEST
    if length_val == 0 and digit_val == 0 and caps_val == 0 and name_val == 0 and email_val == 0 and taken == 0 and signup_password == check_password:
        #Encrypt the users password          
        hashing_pass= hashlib.sha256((signup_password+SALT).encode()) #Hashes signup_password
        hashed_pass = hashing_pass.hexdigest() #^^
        
        #Encrypt the users email
        hashing_email = hashlib.sha256((email+SALT).encode())#Hashes email
        hashed_email = hashing_email.hexdigest() #^^

        if back_col=="black":
            colour_scheme_choice = "monochrome"
        else:
            colour_scheme_choice = "default"

######   CREATES THE DATETIME ELEMENTS:  ####################################################################################################################################
            
        now = date.today()#Get the current date
        instantiating_film_times = []
        for data in range(5): #Create 5 sections for the past 5 days
            past = now - timedelta(days=4-data)
            instantiating_film_times.append("0," + str(past)) #Dont include a forward slash

        print(instantiating_film_times)
        setup_film_times = str(instantiating_film_times) #Turn the list of users watch time into a string 
        setup_film_times = setup_film_times.strip("[]") #Gets rid of the brackets
        setup_film_times = setup_film_times.replace("'","") #Replace the quatation marks with nothing
        print(setup_film_times)
        
##############################################################################################################################################################################

        
        with open("accounts.txt", "a") as accounts: #Opens the file so it can be read from and written to and also be ready to close it self
            accounts.write(hashed_username + "," + hashed_pass + "," + hashed_email + "," + colour_scheme_choice + "/" +
                           setup_film_times + "/place holder\n")#Writes the users details to the account text file

        signup_clear(home_signup, signup_username_entry, signup_password_entry, check_password_entry, email_entry, change_password_format,
                    username_error, password_length_error, password_contents_error, email_error, match_error, taken_error,
                    sign_up_label, username_label, password_label, check_label, email_label, submit, back_col, fore_col, button_col)

def signup_clear(home_signup, signup_username_entry, signup_password_entry, check_password_entry, email_entry, change_password_format,
                   username_error, password_length_error, password_contents_error, email_error, match_error, taken_error,
                   sign_up_label, username_label, password_label, check_label, email_label, submit, back_col, fore_col, button_col):
    #Destroy buttons
    home_signup.destroy()
    change_password_format.destroy()
    submit.destroy()
    
    #Destroyes entries 
    signup_username_entry.destroy()
    signup_password_entry.destroy()
    check_password_entry.destroy()
    email_entry.destroy()
    
    #Destroyes error messages
    username_error.destroy()
    password_length_error.destroy()
    password_contents_error.destroy()
    email_error.destroy()
    match_error.destroy()
    taken_error.destroy()
    
    #Destroyes labels
    sign_up_label.destroy()
    username_label.destroy()
    password_label.destroy()
    check_label.destroy()
    email_label.destroy()

    #Returns to the main menu
    opening(back_col, fore_col, button_col)

def login(back_col, fore_col, button_col):
    main_login_label = Label(root,text = "Please enter your login details", font=("arial",50,"bold"), fg=fore_col, bg=back_col) #This will be the main header for the login function
    main_login_label.place(relx=0.10, rely=0.025) #Places the label at the top of the page
    underline(main_login_label)

    top_login_label = Label(root, text="Username:", font=("arial",25), fg=fore_col, bg=back_col) #Label saying username
    top_login_label.place(relx = 0.05, rely = 0.25) #Placed besides the username entry field

    bottom_login_label = Label(root, text="Password:", font=("arial",25), fg=fore_col, bg=back_col) #Label saying password
    bottom_login_label.place(relx = 0.05, rely = 0.35) #Placed besides the password entry field

    login_username_entry = Entry(root,relief=GROOVE, bd=2, font=("arial",12)) #Username entry field
    login_password_entry = Entry(root,relief=GROOVE, bd=2, font=("arial",12), show = "*") #Password entry field

    login_username_entry.place(relx = 0.20, rely = 0.26, relwidth = 0.2, relheight = 0.05) #Places the both text entry fields on screen
    login_password_entry.place(relx = 0.20, rely = 0.36, relwidth = 0.2, relheight = 0.05) #^^^

    change = Button(text = "", bg = "white", relief=GROOVE, bd=6, command = lambda: show_change(login_password_entry, change))
    change.place(relx=0.41,rely=0.36,relwidth=0.05)
    
    #Creates a button which takes the user to a function
    #lambda allows for parameters to be passed through the button and therefore means less variables have to be globalised
    submit_login_button = Button(text = "Login",font=("arial",20,"bold"), bg=button_col, relief=GROOVE, bd=6,
                                 command = lambda:  home_login.destroy() or logging_in(main_login_label,top_login_label,bottom_login_label,
                                                                                       login_username_entry,login_password_entry,submit_login_button,
                                                                                       forgot_password_link, change,
                                                                                       back_col, fore_col, button_col))
    
    submit_login_button.place(relx = 0.05, rely = 0.45, relwidth = 0.35) # Places the login button on screen

    forgot_password_link = Label(root, text="Forgot Password", fg="blue", bg="snow",relief=GROOVE, bd=6, cursor="hand2", font=("arial",15,"bold"))
    forgot_password_link.place(relx = 0.05, rely = 0.55, relwidth = 0.35)
    forgot_password_link.bind("<Button-1>", lambda event: home_login.destroy() or bottom_login_label.destroy() or login_username_entry.destroy()
                              or login_password_entry.destroy() or submit_login_button.destroy() or forgot_password_link.destroy() or change.destroy() or
                              email_request(main_login_label, top_login_label, back_col, fore_col, button_col))

    #Destroys all objects that are no longer needed
    
    
    

    
    
    #HOME BUTTON FOR THE LOGIN SYSTEM
    home_login = Button(root, text = "Home", font=("arial",15,"bold"), command = lambda:
                  main_login_label.destroy() or top_login_label.destroy()
                  or bottom_login_label.destroy() or login_username_entry.destroy() or login_password_entry.destroy() or
                  submit_login_button.destroy() or forgot_password_link.destroy() or change.destroy() or
                  home_login.destroy() or opening(back_col, fore_col, button_col), bg =button_col, relief=GROOVE, bd=6)
    home_login.place(relx = 0.85, rely = 0.03, relwidth = 0.10, relheight = 0.1)

def logging_in(main_login_label, top_login_label, bottom_login_label,login_username_entry,login_password_entry,submit_login_button,forgot_password_link,change,
               back_col, fore_col, button_col):

    #Retrieves the contents of the two entry widgits
    login_username = login_username_entry.get()
    login_password = login_password_entry.get()
    
    #Destoyes the objects used in the previous function
    main_login_label.destroy()
    top_login_label.destroy()
    bottom_login_label.destroy()
    login_username_entry.destroy()
    login_password_entry.destroy()
    submit_login_button.destroy()
    forgot_password_link.destroy()
    change.destroy()

    failed = True # Declares a boolean variable called failed which will be used to determine if the users details were found or not

    login_username_encrypting = hashlib.sha256((login_username+SALT).encode()) #Hashes login_username
    login_username_encrypted = login_username_encrypting.hexdigest() #^^
    
    login_password_encrypting = hashlib.sha256((login_password+SALT).encode()) #Hashes login_password
    login_password_encrypted = login_password_encrypting.hexdigest() #^^
    
    with open("accounts.txt", "r") as accounts: #Opens the file read only and ready to close it self
        all_data = [line.strip() for line in accounts] #Gets the data from all lines in the accounts text file
        for user in range(len(all_data)): #Gets each users data line by line
            user_data = all_data[user].split(",") #Users data gets set into individual items
            #Reads the first and second item of all lines in the accounts text file
            if user_data[0] == login_username_encrypted and user_data[1].strip(" ") == login_password_encrypted:
                failed = False #If users details are correct than failed = false
            else: #If the test is failed
                pass #Do nothing

    #Creates the outcome label which starts of as if the users details are correct.
    outcome = Label(root,text = "Login Successful", font=("arial",50,"bold"), fg = "lime", bg = "black")
    
    if failed == False: #If user logs in successfully then,
        outcome.place(relx = 0.25, rely = 0.35) #Place the label on screen
        continue_button = Button(text = "Continue",font=("arial",20,"bold"),bg = "mistyrose", relief=GROOVE, bd=6,command = lambda:
                                 outcome.destroy() or continue_button.destroy() or setup(login_username_encrypted, back_col, fore_col, button_col))
        continue_button.place(relx = 0.38, rely = 0.50)
        #This button also destroys the outcome label, the background image as well as itself when it is pressed^^^
    
    else: #If the users details are not found to be in the accounts file
        outcome["text"] = "Login Failed" #Change the outcome labels text to Login Failed
        outcome["fg"] = "red" #Change the outcome labels foreground colour to red
        outcome.place(relx = 0.35, rely = 0.35) #Place the label on screen
        #Create a button and place it on the screen that allows the user to be taken back to login screen
        return_button = Button(text = "Return to login screen",font=("arial",20,"bold"),
                               bg = "mistyrose", relief=GROOVE, bd=6,command = lambda: outcome.destroy() or return_button.destroy() or login(back_col, fore_col, button_col))
        return_button.place(relx = 0.38, rely = 0.50) #This button also destroys the outcome label as well as itself when it is pressed^^^


def email_request(main_login_label, top_login_label, back_col, fore_col, button_col):
    
    main_login_label["text"] = "Reset your password:" #Changes the main_login_label so it reads "Reset your pasword:"
    top_login_label["text"] = "Email:" #top_login_label is reused to represent the email label

    
    #A new entry field is created for the users email as reusing login_username_entry would could have caused slight naming issues
    login_email_entry = Entry(root,relief=GROOVE, bd=2, font=("arial",12))
    login_email_entry.place(relx = 0.15, rely = 0.255, relwidth = 0.2, relheight = 0.05) #Places the text entry box on screen
    checking_email_button = Button(text = "Next",font=("arial",20,"bold"), bg="mistyrose", relief=GROOVE, bd=6, command = lambda:
                                   home_from_email_request.destroy() or
                                   email_check(main_login_label,
                                               top_login_label,
                                               login_email_entry,
                                               checking_email_button,
                                               back_col, fore_col, button_col))
    
    checking_email_button.place(relx = 0.05, rely = 0.35, relwidth = 0.2)

    #HOME BUTTON FROM THE EMAIL_REQUEST FUNCTION
    home_from_email_request = Button(root, text = "Home", font=("arial",15,"bold"), command = lambda:
                                     home_from_email_request.destroy() or checking_email_button.destroy() or
                                     login_email_entry.destroy() or checking_email_button.destroy() or
                                     top_login_label.destroy() or main_login_label.destroy() or
                                     opening(), bg ="pink", activebackground = "hotpink", relief=GROOVE, bd=6)
    home_from_email_request.place(relx = 0.85, rely = 0.03, relwidth = 0.10, relheight = 0.1)

def email_check(main_login_label, top_login_label,login_email_entry,checking_email_button, back_col, fore_col, button_col):
    checking_email_button.destroy() #Destroys the button used to submit the users email
    login_email = login_email_entry.get() #Retrieves the users email
    login_email_encrypting = hashlib.sha256((login_email+SALT).encode()) #Hashes login_email
    login_email_encrypted = login_email_encrypting.hexdigest() #^^
    email_not_found = Label(root,text = "EMAIL NOT FOUND", font=("arial",50,"bold"), fg = "red", bg = "black")
    email_not_found.place(relx = 0.25, rely = 0.35)
    found = False
    with open("accounts.txt", "r+") as accounts: #Opens the file read only and ready to close it self
        all_data = [line.strip() for line in accounts] #Gets the data from all lines in the accounts text file
        for users_email in range(len(all_data)): #Gets each users data line by line
            user_data = all_data[users_email].split(",") #Users data gets set into individual items
            if user_data[2] == login_email_encrypted: #Strip the read email so the actual email can be compared to login_email
                found = True
            else: #If the test is failed
                pass
            
    if found == False: #If the users email is not found
        #Destroy all on screen objects ready to return to the login function
        main_login_label.destroy()
        top_login_label.destroy()
        login_email_entry.destroy()
        return_login_button = Button(text = "Return to login screen",font=("arial",20,"bold"),bg="mistyrose", relief=GROOVE, bd=6,
                                     command = lambda: email_not_found.destroy() or return_login_button.destroy() or login(back_col, fore_col, button_col))
        return_login_button.place(relx = 0.35, rely = 0.50)
    
    elif found == True: #If the users email is found
        email_not_found.destroy() #Destroys the label which tells the user the email was not found
        login_email_entry.destroy() #Destroys the email entry box as it is no longer needed
        password_request(main_login_label, top_login_label, login_email_encrypted, back_col, fore_col, button_col)

def password_request(main_login_label, top_login_label, login_email_encrypted, back_col, fore_col, button_col):
    top_login_label["text"] = "New Password:" #Changes the top_login_label text to read "New Password"
    #Creates and places a new text entry box which will be used to enter the users new password
    length_error = Label(root, text = "Password must be atleast 10 characters", font=("arial",15, "bold"), fg = "red", bg = "black")
    num_error = Label(root, text = "Password must contain atleast one number", font=("arial",15, "bold"), fg = "red", bg = "black")
    caps_error = Label(root, text = "Password must contain atleast one capital letter", font=("arial",15, "bold"), fg = "red", bg = "black")
    login_new_password_entry = Entry(root,relief=GROOVE, bd=2, font=("arial",12))
    login_new_password_entry.place(relx = 0.25, rely = 0.25, relwidth = 0.2, relheight = 0.05) #Places the text entry box on screen
    checking_password_button = Button(text = "Next",font=("arial",20,"bold"), bg="mistyrose",command = lambda: home_from_password_request.destroy() or
                                      validating_new_password(main_login_label,
                                                              top_login_label,
                                                              login_new_password_entry,
                                                              login_email_encrypted,
                                                              checking_password_button,
                                                              length_error, num_error, caps_error,
                                                              back_col, fore_col, button_col))
    
    checking_password_button.place(relx = 0.05, rely = 0.45, relwidth = 0.2)

    #HOME BUTTON FROM THE PASSWORD_REQUEST FUNCTION
    home_from_password_request = Button(root, text = "Home", font=("arial",15,"bold"), command = lambda: top_login_label.destroy() or
                                        main_login_label.destroy() or length_error.destroy() or num_error.destroy() or
                                        caps_error.destroy() or login_new_password_entry.destroy() or checking_password_button.destroy() or
                                        home_from_password_request.destroy() or
                                     opening(back_col, fore_col, button_col), bg ="pink", activebackground = "hotpink", relief=GROOVE, bd=6)
    home_from_password_request.place(relx = 0.85, rely = 0.03, relwidth = 0.10, relheight = 0.1)

def validating_new_password(main_login_label, top_login_label, login_new_password_entry, login_email_encrypted,
                            checking_password_button,
                            length_error, num_error, caps_error,
                            back_col, fore_col, button_col):
    
    new_password = login_new_password_entry.get()
    
    #Boolean values used determine if all tests are passed  
    new_digit_val = 1 #Password digit test
    new_length_val = 1 #Password length test
    new_caps_val = 1 #Password capital letter test
    
    #Password Validation  
    if len(new_password) >= 10: #If the users password is 10 or more character long
        length_error.place_forget() #Hide the length_error label
        new_length_val = 0 #Class the test as passed
        
    elif len(new_password) == 0:
        length_error.place(relx = 0.52, rely = 0.26) #Place the length_error label on screen
        new_length_val = 1 #And class the test as failed

        num_error.place(relx = 0.52, rely = 0.32) #Place the num_error label on screen
        new_digit_val = 1 #And class the test as failed

        caps_error.place(relx = 0.52, rely = 0.38) #Place the caps_error label on screen
        new_caps_val = 1 #And class the test as failed
        
    else: #Otherwise
        length_error.place(relx = 0.52, rely = 0.26) #Place the length_error label on screen
        new_length_val = 1 #And class the test as failed
                        

    for digit in range(len(new_password)): #For length of password
        if new_password[digit].isdigit(): #Checks each individual character to see if its a number
            num_error.place_forget() #Hide the num_error label
            new_digit_val = 0 #Class the test as passed
            break #Ends current for loop
        else: #Otherwise
            num_error.place(relx = 0.52, rely = 0.32) #Place the num_error label on screen
            new_digit_val = 1 #And class the test as failed
            
        
    for caps in range(len(new_password)): #For length of password
        if new_password[caps].isupper(): #Checks each individual character to see if its a capital letter
            caps_error.place_forget() #Hide the caps_error label
            new_caps_val = 0 #Class the test as passed
            break
        else: #Otherwise
            caps_error.place(relx = 0.52, rely = 0.38) #Place the caps_error label on screen
            new_caps_val = 1 #And class the test as failed
    
    #OUTCOME TEST
    if new_length_val == 0 and new_digit_val == 0 and new_caps_val == 0: #If all test are passed go to the updating password function
        updating_password(main_login_label, top_login_label,login_new_password_entry, new_password,
                          login_email_encrypted,checking_password_button,
                          back_col, fore_col, button_col)
    else: #Otherwise
        pass #Do nothing
        
def writing_password(users_old_password, new_encrypted_password, login_email_encrypted, user_details, user_watch_time, user_film_choices, user_film_choices_list,
                     back_col, fore_col, button_col):
    
    new_user_data = "" #This is the variable that will eventually contain all of the users new details

    #Formats the users details
    for finalised_user_details in range(len(user_details)):
        if finalised_user_details == len(user_details)-1:
            new_user_data = new_user_data + user_details[finalised_user_details].strip() + "/"
            print("password end",new_user_data)
        elif finalised_user_details == 1:
            new_user_data = new_user_data + new_encrypted_password.strip() + ","
            print("password",new_user_data)
        else:
            new_user_data = new_user_data + user_details[finalised_user_details].strip() + ","
            print("normal",new_user_data)
            
    #THIS LIMITS THE AMOUNT OF DATA THAT CAN BE STORED ON A USERS ACCOUNT TO THE 200 MOST RECENT ELEMENTS. THIS IS TO MAKE THE SUGGESTIONS RELEVANT AND UP TO DATE
    print("user_film_choices_list",user_film_choices_list)
    while len(user_film_choices_list)>200:
        del user_film_choices_list[0]

    #TURNING A LIST INTO A STRING WITH CORRECT FORMATTING

    user_watch_time = str(user_watch_time)
    user_watch_time=user_watch_time.replace("[","")#removes left bracket
    user_watch_time=user_watch_time.replace("]","")#removes right bracket
    user_watch_time=user_watch_time.replace('"',"")#removes "
    user_watch_time=user_watch_time.replace(' ',"")#removes all spaces
    user_watch_time=user_watch_time.replace("'","")#removes '

    new_user_data = new_user_data + user_watch_time + "/"
    print("\n\n\n\n\n",new_user_data)
        
    user_film_choices_list = str(user_film_choices_list)
    user_film_choices_list=user_film_choices_list.replace("[","")#removes left bracket
    user_film_choices_list=user_film_choices_list.replace("]","")#removes right bracket
    user_film_choices_list=user_film_choices_list.replace('"',"")#removes "
    user_film_choices_list=user_film_choices_list.replace(' ',"")#removes all spaces
    user_film_choices_list=user_film_choices_list.replace("'","")#removes '
    

    new_user_data = new_user_data + user_film_choices_list
    print("\n\n\n\n\n",new_user_data)

    #print(user_film_choices_list[0][finalised_user_film_choices].strip(""))
    #Rewrites the users details in the new, correct, form        
    with open("accounts.txt", "r+") as accounts: #Opens the file so it can be read from and written to and also be ready to close it self
        all_data = [line.strip() for line in accounts] #Gets the data from all lines in the accounts text file
        for user in range(len(all_data)): #Gets each users data line by line
            user_data = all_data[user].split(",") #Users data gets set into individual items
            if user_data[2].strip() == login_email_encrypted: #Reads the first item of all lines in the accounts text file
                del all_data[user] #Removes the data that is currently stored for the user
                accounts.truncate(0) #Clears the accounts file
                accounts.seek(0,0) #Sets the pointer to the beginning of the file
                for all_users in range(len(all_data)): #For each line in the accounts text file
                    accounts.write(all_data[all_users]+"\n") #Rewrite the line and start a new one
                accounts.seek(0,2)#Sets the pointer to the end of the file
                accounts.write(new_user_data) #Rewrites the old details and adds the contents of user_dislikes
                break #end for loop
            else:
                pass #Increment user by one

    print(new_user_data)
    login(back_col, fore_col, button_col)
            
def updating_password(main_login_label, top_login_label,login_new_password_entry, new_password, login_email_encrypted,checking_password_button,back_col, fore_col, button_col):
    #Destroys the objects that are no longer needed and retrieves the contents of login_new_password_entry
    main_login_label.destroy()
    top_login_label.destroy()
    login_new_password_entry.destroy()
    checking_password_button.destroy()
    with open("accounts.txt", "r+") as accounts: #Opens the file read only and ready to close it self
        all_data = [line.strip() for line in accounts] #Gets the data from all lines in the accounts text file
        for users_email in range(len(all_data)): #Gets each users data line by line
            user_data = all_data[users_email].split(",") #Users data gets set into individual items
            if user_data[2].strip() == login_email_encrypted: #Strip the read email so the actual email can be compared to login_email
                #Updating the users password
                users_old_password = user_data[1] #Retrieves the users old password so the system knows what to replace
                account_needs_updating = users_email #Retrieves the value of the for loop counter so the system knows what line needs to be replaced
                new_encrypting = hashlib.sha256((new_password+SALT).encode()) #Hashes login_email
                new_encrypted_password = new_encrypting.hexdigest() #^^
                
                user_data = str(user_data) #Turns the user_data into a string so it can be split 
                user_data = user_data.strip("[]") #Strips user_data of square brackets
                
                user_details, user_watch_time, user_film_choices = user_data.split("/")
                user_film_choices_list=[]
                user_film_choices_list.append(user_film_choices.split(","))
                #Strips user data where ever there is a "/" ^
                
                #Getting user_details into a readable format
                user_details = user_details.replace("'", "") #Replaces the quatation marks with empty space
                user_details = user_details.split(",") #Splits the string where ever there is a comma

                break
            
    writing_password(users_old_password, new_encrypted_password, login_email_encrypted, user_details, user_watch_time, user_film_choices, user_film_choices_list,
                     back_col, fore_col, button_col)

def setup(login_username_encrypted, back_col, fore_col, button_col):

    watched_time_list = []
    
    #Reads the account list to retrieve and store appropriate data
    with open("accounts.txt", "r") as accounts: #Opens the file read only and ready to close it self
        all_data = [line.strip() for line in accounts] #Gets the data from all lines in the accounts text file
        for user in range(len(all_data)): #Gets each users data line by line
            user_data = all_data[user].split(",") #Users data gets set into individual items
            if user_data[0] == login_username_encrypted: #Reads the first item of all lines in the accounts text file
                user_data = str(user_data) #Turns the user_data into a string so it can be split 
                user_data = user_data.strip("[]") #Strips user_data of square brackets
                user_details, user_time_watched, users_past_choices = user_data.split("/")
                #Strips user data where ever there is a "/" ^
                
                #Getting user_details into a readable format
                user_details = user_details.replace("'", "") #Replaces the quatation marks with empty space
                user_details = user_details.split(",") #Splits the string where ever there is a comma

                #Gets user_time_watched into a readable format
                watched_time_sort(user_time_watched, watched_time_list)
                
                #Getting user_past_choices into a readable format
                users_past_choices = users_past_choices.replace("'", "") #Replaces the quatation marks with empty space
                users_past_choices = users_past_choices.split(",") #Splits the string where ever there is a comma
                user_film_choices = []
                for edit in range(len(users_past_choices)): #For the length of users_past_choices
                    user_film_choices.append(users_past_choices[edit].strip(" ")) #Append each index stripped to a seperate list
                    
                if user_details[3].strip() == "posh":
                    scheme="posh"
                    back_col="snow"
                    fore_col="lightgoldenrod1"
                    button_col="lightgoldenrod1"
                    
                elif user_details[3].strip() == "monochrome":
                    scheme="monochrome"
                    back_col="black"
                    fore_col="white"
                    button_col="white"
                    
                elif user_details[3].strip() == "matrix":
                    scheme="matrix"
                    back_col="black"
                    fore_col="lime"
                    button_col="lime"

                elif user_details[3].strip() == "colour splash":
                    scheme="colour splash"
                    back_col="yellow"
                    fore_col="blue"
                    button_col="red"

                elif user_details[3].strip() == "default":
                    scheme="default"
                    back_col="steelblue"
                    fore_col="lightgoldenrod1"
                    button_col="pink"
                    
                elif user_details[3].strip() == "toxic":
                    scheme="toxic"
                    back_col="green"
                    fore_col="yellow"
                    button_col="lime"
                
    non_readable_film_list = [] #A version of the film_list but not in the desired readable form
    with open("films.txt", "r") as films: #Opens the file read only and ready to close it self
        for line in films:
            non_readable_film_list.append(line.strip(" ")) #Appends each line of the films text file to a list

        singular_film_index_list = [] # Creates a list that is designed to store one item at a time
        film_list = [] #Creates a list in which the contents of singular_film_index_list are appended to
        for formatting in range(len(non_readable_film_list)): #For every film in non_readable_film_list
            for index_formatting in range(len(non_readable_film_list[formatting].split(","))): #For each data element of a certain film
                #Append each film stripped to singular_film_index_list
                singular_film_index_list.append(non_readable_film_list[formatting].split(",")[index_formatting].strip())
                
            film_list.append(singular_film_index_list)#Append all the data stored for one film item to film_list
            singular_film_index_list = [] #Clears the list so it can be reused

    watch_time_update(watched_time_list, 0) #Updates watched_time_list but does not add an additional value

    main(user_details, user_film_choices, film_list, login_username_encrypted, back_col, fore_col, button_col, scheme, watched_time_list)

def watched_time_sort(user_time_watched, watched_time_list): #Used o sort the users watch time into a readable format
    user_time_watched = user_time_watched.replace("'", "") #Replaces the quatation marks with empty space
    user_time_watched = user_time_watched.split(",") #Splits the string where ever there is a comma
    for x in range(0,len(user_time_watched),2): #For the range of watch time (should be 10)
        watched_time_list.append(user_time_watched[x] + user_time_watched[x+1]) #Append each data of watch time along with its relevent date to a list


def watch_time_update(watched_time_list, additional_data):
    dates = [] #This is a list of the dates stored in watched_time_list
    updated = False #No data had been updated
    
    for data in range(len(watched_time_list)):#For the length of the watched_time_list
        #print((watched_time_list[data].strip()))
        watch_time_value, date_stored = watched_time_list[data].strip().split(" ", 2)#Split the stripped list to get the value and the date seperately
        dates.append(date_stored)#Appends the stored date to the dates list
        
    for updating_watch_time_data in range(len(watched_time_list)):#For the length of the watched_time_list
        stored_date = time.strptime(dates[updating_watch_time_data], "%Y-%m-%d")#formats the stored dates into the form year-month-day
        now = date.today()#Get the current date
        past = now - timedelta(days=4-updating_watch_time_data)#past equals the current date -x ammount of days
        checking_past = time.strptime(str(past), "%Y-%m-%d")#formats the past date into the form year-month-day
        #Now the dates are in the correct form comparisons can take place
        if str(past) in dates: #If past is in the dates list
            for search in range(len(dates)):#length of dates
                if str(past) == dates[search]:#If past is equal to dates[search]
                    index = search#Store the current index in a variable called index
                else:#Otherwise,
                    pass#Do nothing

            #Splits each index of watched_time_list into the stored value and its date
            watch_time_value, irrelevent_date = watched_time_list[index].strip().split(" ", 2)
        
            if dates[index] == str(now): #If a date in the dates list is equal to the date now
                new_watch_time_value = int(watch_time_value) + additional_data
                #The new watch time value equals the old value plus the additional value supplied^
                watched_time_list[updating_watch_time_data] = str(new_watch_time_value) + " " + str(now)
                #The new version of this index is equal to new_watch_time_value plus a space plus the current date^
                updated = True #Data has now been updated
                
            else: #Otherwise
                watched_time_list[updating_watch_time_data] = watch_time_value + " " + str(past)
                #The new version of this index is equal to watch_time_value plus a space plus the date currently being used as the past^
                    
        elif checking_past > stored_date: #If checking_past is greater than the stored date
            watched_time_list[updating_watch_time_data] = "0 " + str(past)
            #Index now is set to being equal to "0 " plus the date past
            
        else: #Otherwise
            pass #Do nothing
    
def main(user_details, user_film_choices, film_list, login_username_encrypted, back_col, fore_col, button_col, scheme, watched_time_list):
    
    root.bind('<Escape>', lambda event: closed_update(user_details, user_film_choices, login_username_encrypted, scheme, watched_time_list)) #Binds the escape key to the function named closed
    root.protocol("WM_DELETE_WINDOW", lambda event: closed_update(user_details, user_film_choices, login_username_encrypted, scheme, watched_time_list)) #When the window is attempted to be closed go to the close function
    root.config(bg = back_col)
    #Label for title
    menu_title = Label(root,text = "Welcome to VMedia", font=("arial",50,"bold"), fg = fore_col, bg = back_col) #Creates a label menu_title to welcome the user to VMedia
    menu_title.pack(side = "top") #Outputs the label at the top of the window
    underline(menu_title)


    non_readable_film_list=[]
    with open("films.txt", "r") as films: #Opens the file read only and ready to close it self
        for line in films:
            non_readable_film_list.append(line.strip(" ")) #Appends each line of the films text file to a list

        singular_film_index_list = [] # Creates a list that is designed to store one item at a time
        film_list = [] #Creates a list in which the contents of singular_film_index_list are appended to
        for formatting in range(len(non_readable_film_list)): #For every film in non_readable_film_list
            for index_formatting in range(len(non_readable_film_list[formatting].split(","))): #For each data element of a certain film
                #Append each film stripped to singular_film_index_list
                singular_film_index_list.append(non_readable_film_list[formatting].split(",")[index_formatting].strip())
                
            film_list.append(singular_film_index_list)#Append all the data stored for one film item to film_list
            singular_film_index_list = [] #Clears the list so it can be reused

            
    #signout
    #Creates a button that will allow the user to signout of the system so they can use a different account if they wish
    sign_out_button = Button(root, text = "sign out", font=("arial",10,"bold"), bg = button_col,
                             command = lambda: closed_update(user_details, user_film_choices, login_username_encrypted, scheme, watched_time_list), relief=GROOVE, bd=6)
    sign_out_button.place(relx=0.075, rely=0.06, relwidth = 0.1, relheight = 0.1, anchor = "center")


    #This button takes the user to the graphing function where the graph of watch time against time is plotted
    graph_button = Button(root, text = "Graph", font = ("arial", 10, "bold"),
                           bg = button_col, command = lambda: graphing(watched_time_list), relief=GROOVE, bd=6)
    graph_button.place(relx = 0.20, rely = 0.06, relwidth = 0.1, relheight = 0.1, anchor = "center")

    
    #Creates a entry field to resemble the one that will be there in the full system
    search_entry = Entry(root,relief=GROOVE, bd=2, font=("arial",20)) # ^^
    search_entry.place(relx = 0.56, rely = 0.2, relwidth = 0.3)

    #This button submits your search request
    search_button = Button(root, text = "Search", font = ("arial", 10, "bold"),
                           bg = button_col, command = lambda:
                           callback_a(list_of_films, hyperlink, film_list, user_film_choices,
               menu_title, scroll_bar, colour_schemes_button, user_details, login_username_encrypted
                                 , back_col, fore_col, button_col, scheme, watched_time_list,
                                 sign_out_button, search_entry, revert_button,
                                   filter_heading_label, disney_label, disney_button, action_label, action_button,
                                   adventure_label, adventure_button, comedy_label, comedy_button, romance_label,
                                   romance_button, horror_label, horror_button, dc_label, dc_button,
                                 chick_flicks_label, chick_flicks_button, sci_fi_label, sci_fi_button,
                                   musicals_label, musicals_button, classics_label, classics_button,
                                   thriller_label, thriller_button, fantasy_label, fantasy_button,
                                   marvel_label, marvel_button, graph_button, submit_filters, search_button, True), relief=GROOVE, bd=6)
    search_button.place(relx = 0.87, rely = 0.2, relwidth = 0.05, relheight = 0.05)

    #This button returns the films list to the normal AI recommended state
    revert_button = Button(root, text = "revert", font = ("arial", 10, "bold"),
                           bg = button_col, command = lambda:
                           callback_a(list_of_films, hyperlink, film_list, user_film_choices,
               menu_title, scroll_bar, colour_schemes_button, user_details, login_username_encrypted
                                 , back_col, fore_col, button_col, scheme, watched_time_list,
                                 sign_out_button, revert_button,
                                   filter_heading_label, disney_label, disney_button, action_label, action_button,
                                   adventure_label, adventure_button, comedy_label, comedy_button, romance_label,
                                   romance_button, horror_label, horror_button, dc_label, dc_button,
                                 chick_flicks_label, chick_flicks_button, sci_fi_label, sci_fi_button,
                                   musicals_label, musicals_button, classics_label, classics_button,
                                   thriller_label, thriller_button, fantasy_label, fantasy_button,
                                   marvel_label, marvel_button, graph_button, submit_filters, search_button, search_entry, revert=True), relief=GROOVE, bd=6)
    revert_button.place(relx = 0.93, rely = 0.2, relwidth = 0.05, relheight = 0.05)

    
    #Colour schemes button
    colour_schemes_button = Button(root, text="Colour Schemes", font=("arial",12,"bold"), bg=button_col, command = lambda:
                                   menu_title.destroy() or list_of_films.destroy() or search_button.destroy() or scroll_bar.destroy() or colour_schemes_button.destroy()
                                   or sign_out_button.destroy() or search_entry.destroy() or revert_button.destroy() or
                                   filter_heading_label.destroy() or disney_label.destroy() or disney_button.destroy() or action_label.destroy() or action_button.destroy() or
                                   adventure_label.destroy() or adventure_button.destroy() or comedy_label.destroy() or comedy_button.destroy() or romance_label.destroy() or
                                   romance_button.destroy() or horror_label.destroy() or horror_button.destroy() or dc_label.destroy() or dc_button.destroy() or
                                   chick_flicks_label.destroy() or chick_flicks_button.destroy() or sci_fi_label.destroy() or sci_fi_button.destroy() or
                                   musicals_label.destroy() or musicals_button.destroy() or classics_label.destroy() or classics_button.destroy() or
                                   thriller_label.destroy() or thriller_button.destroy() or fantasy_label.destroy() or fantasy_button.destroy() or
                                   marvel_label.destroy() or marvel_button.destroy() or graph_button.destroy() or submit_filters.destroy() or
                                   colour_schemes(user_details, user_film_choices, film_list, login_username_encrypted,
                                                  back_col,fore_col,button_col,scheme, watched_time_list), relief=GROOVE, bd=6)
    
    colour_schemes_button.place(relx=0.85, rely=0.06, relwidth = 0.17, relheight = 0.1, anchor = "center") #Places the button exactly where I want it in relation to the size of the root window and centralises it

    #Creates a text box for all the films to be written to along with a scroll bar so the contents are not limited
    list_of_films = Text(root,wrap=WORD,cursor = "arrow",bd=8, relief=GROOVE, font=("arial",17, "bold"), fg=fore_col, bg = back_col)
    list_of_films.place(relx=0.005, rely=0.15, relwidth = 0.53, relheight = 0.8) #Displays the text box to the user
    scroll_bar = Scrollbar(root)
    scroll_bar.place(relx = 0.54, rely = 0.15, relheight = 0.8)
    scroll_bar.config(command=list_of_films.yview)
    list_of_films.config(yscrollcommand=scroll_bar.set)


    #################################

    #CREATES THE FILTER SYSTEM:
    filter_heading_label = Label(root,text = "Filters", font=("arial",20,"bold"), fg = fore_col, bg = back_col)
    filter_heading_label.place(relx=0.65, rely=0.3, relwidth = 0.17, relheight = 0.1, anchor = "center")
    underline(filter_heading_label)
    

    #disney
    disney_check = BooleanVar()

    disney_label = Label(root, text = "Disney", font=("arial",15,"bold"),fg = fore_col, bg = back_col)
    disney_label.place(relx = 0.62, rely = 0.33)
    
    disney_button = Checkbutton(root, variable = disney_check,bg = "black",relief=GROOVE, bd=6)
    disney_button.place(relx = 0.70, rely = 0.33)


    #action
    action_check = BooleanVar()

    action_label = Label(root, text = "Action", font=("arial",15,"bold"),fg = fore_col, bg = back_col)
    action_label.place(relx = 0.62, rely = 0.38)
    
    action_button = Checkbutton(root, variable = action_check,bg = "black",relief=GROOVE, bd=6)
    action_button.place(relx = 0.70, rely = 0.38)


    #adventure
    adventure_check = BooleanVar()
    
    adventure_label = Label(root, text = "Adventure", font=("arial",15,"bold"),fg = fore_col, bg = back_col)
    adventure_label.place(relx = 0.62, rely = 0.43)
    
    adventure_button = Checkbutton(root, variable = adventure_check,bg = "black",relief=GROOVE, bd=6)
    adventure_button.place(relx = 0.70, rely = 0.43)


    #comedy
    comedy_check = BooleanVar()
    
    comedy_label = Label(root, text = "Comedy", font=("arial",15,"bold"),fg = fore_col, bg = back_col)
    comedy_label.place(relx = 0.62, rely = 0.48)
    
    comedy_button = Checkbutton(root, variable = comedy_check,bg = "black",relief=GROOVE, bd=6)
    comedy_button.place(relx = 0.70, rely = 0.48)


    #romance
    romance_check = BooleanVar()
    
    romance_label = Label(root, text = "Romance", font=("arial",15,"bold"),fg = fore_col, bg = back_col)
    romance_label.place(relx = 0.62, rely = 0.53)
    
    romance_button = Checkbutton(root, variable = romance_check,bg = "black",relief=GROOVE, bd=6)
    romance_button.place(relx = 0.70, rely = 0.53)


    #horror
    horror_check = BooleanVar()
    
    horror_label = Label(root, text = "Horror", font=("arial",15,"bold"),fg = fore_col, bg = back_col)
    horror_label.place(relx = 0.62, rely = 0.58)
    
    horror_button = Checkbutton(root, variable = horror_check,bg = "black",relief=GROOVE, bd=6)
    horror_button.place(relx = 0.70, rely = 0.58)


    #DC
    dc_check = BooleanVar()
    
    dc_label = Label(root, text = "DC", font=("arial",15,"bold"),fg = fore_col, bg = back_col)
    dc_label.place(relx = 0.62, rely = 0.63)
    
    dc_button = Checkbutton(root, variable = dc_check,bg = "black",relief=GROOVE, bd=6)
    dc_button.place(relx = 0.70, rely = 0.63)


    #Chick Flicks
    chick_flicks_check = BooleanVar()
    
    chick_flicks_label = Label(root, text = "Chick Flicks", font=("arial",15,"bold"),fg = fore_col, bg = back_col)
    chick_flicks_label.place(relx = 0.76, rely = 0.33)

    chick_flicks_button = Checkbutton(root, variable = chick_flicks_check,bg = "black",relief=GROOVE, bd=6)
    chick_flicks_button.place(relx = 0.86, rely = 0.33)


    #Sci-Fi
    sci_fi_check = BooleanVar()
    
    sci_fi_label = Label(root, text = "Sci-Fi", font=("arial",15,"bold"),fg = fore_col, bg = back_col)
    sci_fi_label.place(relx = 0.76, rely = 0.38)

    sci_fi_button = Checkbutton(root, variable = sci_fi_check,bg = "black",relief=GROOVE, bd=6)
    sci_fi_button.place(relx = 0.86, rely = 0.38)
    

    #Musicals
    musicals_check = BooleanVar()
    
    musicals_label = Label(root, text = "Musicals", font=("arial",15,"bold"),fg = fore_col, bg = back_col)
    musicals_label.place(relx = 0.76, rely = 0.43)

    musicals_button = Checkbutton(root, variable = musicals_check,bg = "black",relief=GROOVE, bd=6)
    musicals_button.place(relx = 0.86, rely = 0.43)
    

    #Classics
    classics_check = BooleanVar()
    
    classics_label = Label(root, text = "Classics", font=("arial",15,"bold"),fg = fore_col, bg = back_col)
    classics_label.place(relx = 0.76, rely = 0.48)

    classics_button = Checkbutton(root, variable = classics_check,bg = "black",relief=GROOVE, bd=6)
    classics_button.place(relx = 0.86, rely = 0.48)
    
    #Thriller
    thriller_check = BooleanVar()
    
    thriller_label = Label(root, text = "Thriller", font=("arial",15,"bold"),fg = fore_col, bg = back_col)
    thriller_label.place(relx = 0.76, rely = 0.53)

    thriller_button = Checkbutton(root, variable = thriller_check,bg = "black",relief=GROOVE, bd=6)
    thriller_button.place(relx = 0.86, rely = 0.53)

    
    #Fantasy
    fantasy_check = BooleanVar()
    
    fantasy_label = Label(root, text = "Fantasy", font=("arial",15,"bold"),fg = fore_col, bg = back_col)
    fantasy_label.place(relx = 0.76, rely = 0.58)

    fantasy_button = Checkbutton(root, variable = fantasy_check,bg = "black",relief=GROOVE, bd=6)
    fantasy_button.place(relx = 0.86, rely = 0.58)
    
    #Marvel
    marvel_check = BooleanVar()
    
    marvel_label = Label(root, text = "Marvel", font=("arial",15,"bold"),fg = fore_col, bg = back_col)
    marvel_label.place(relx = 0.76, rely = 0.63)
    
    marvel_button = Checkbutton(root, variable = marvel_check,bg = "black",relief=GROOVE, bd=6)
    marvel_button.place(relx = 0.86, rely = 0.63)

    
    submit_filters = Button(root, text = "Activate filter settings", font=("arial",15,"bold"),
                            command = lambda: check_filters(list_of_films, hyperlink, film_list, user_film_choices,
               menu_title, scroll_bar, colour_schemes_button, user_details, login_username_encrypted
                                 , back_col, fore_col, button_col, scheme, watched_time_list,
                                 sign_out_button, search_entry, revert_button,
                                   filter_heading_label, disney_label, disney_button, action_label, action_button,
                                   adventure_label, adventure_button, comedy_label, comedy_button, romance_label,
                                   romance_button, horror_label, horror_button, dc_label, dc_button,
                                 chick_flicks_label, chick_flicks_button, sci_fi_label, sci_fi_button,
                                   musicals_label, musicals_button, classics_label, classics_button,
                                   thriller_label, thriller_button, fantasy_label, fantasy_button,
                                   marvel_label, marvel_button, graph_button, submit_filters, search_button,
                                disney_check, action_check, adventure_check,
                  comedy_check, romance_check, horror_check, dc_check, chick_flicks_check, sci_fi_check, musicals_check,
                  classics_check, thriller_check, fantasy_check, marvel_check), bg = button_col,relief=GROOVE, bd=6)
    
    submit_filters.place(relx = 0.60, rely = 0.75, relwidth = 0.3, relheight = 0.1) #Places the submit button on screen.

    ##############
    hyperlink = HyperlinkManager(list_of_films, menu_title, list_of_films, scroll_bar, colour_schemes_button, user_details, user_film_choices, film_list, login_username_encrypted
                                 , back_col, fore_col, button_col, scheme, watched_time_list,
                                 sign_out_button, search_entry, revert_button,
                                   filter_heading_label, disney_label, disney_button, action_label, action_button,
                                   adventure_label, adventure_button, comedy_label, comedy_button, romance_label,
                                   romance_button, horror_label, horror_button, dc_label, dc_button,
                                 chick_flicks_label, chick_flicks_button, sci_fi_label, sci_fi_button,
                                   musicals_label, musicals_button, classics_label, classics_button,
                                   thriller_label, thriller_button, fantasy_label, fantasy_button,
                                   marvel_label, marvel_button, graph_button, submit_filters, search_button)
    
    callback_a(list_of_films, hyperlink, film_list, user_film_choices,
               menu_title, scroll_bar, colour_schemes_button, user_details, login_username_encrypted
                                 , back_col, fore_col, button_col, scheme, watched_time_list,
                                 sign_out_button, search_entry, revert_button,
                                   filter_heading_label, disney_label, disney_button, action_label, action_button,
                                   adventure_label, adventure_button, comedy_label, comedy_button, romance_label,
                                   romance_button, horror_label, horror_button, dc_label, dc_button,
                                 chick_flicks_label, chick_flicks_button, sci_fi_label, sci_fi_button,
                                   musicals_label, musicals_button, classics_label, classics_button,
                                   thriller_label, thriller_button, fantasy_label, fantasy_button,
                                   marvel_label, marvel_button, graph_button, submit_filters, search_button) #Go to call back and pass in the parameters list_of_films and hyperlink

#filter system:
def check_filters(list_of_films, hyperlink, film_list, user_film_choices,
               menu_title, scroll_bar, colour_schemes_button, user_details, login_username_encrypted
                                 , back_col, fore_col, button_col, scheme, watched_time_list,
                                 sign_out_button, search_entry, revert_button,
                                   filter_heading_label, disney_label, disney_button, action_label, action_button,
                                   adventure_label, adventure_button, comedy_label, comedy_button, romance_label,
                                   romance_button, horror_label, horror_button, dc_label, dc_button,
                                 chick_flicks_label, chick_flicks_button, sci_fi_label, sci_fi_button,
                                   musicals_label, musicals_button, classics_label, classics_button,
                                   thriller_label, thriller_button, fantasy_label, fantasy_button,
                                   marvel_label, marvel_button, graph_button, submit_filters, search_button,

                  disney_check, action_check, adventure_check,
                  comedy_check, romance_check, horror_check, dc_check, chick_flicks_check, sci_fi_check, musicals_check,
                  classics_check, thriller_check, fantasy_check, marvel_check):
    
    disney = disney_check.get()
    action = action_check.get()
    adventure = adventure_check.get()
    comedy = comedy_check.get()
    romance = romance_check.get()
    horror = horror_check.get()
    dc = dc_check.get()
    chick_flicks = chick_flicks_check.get()
    sci_fi = sci_fi_check.get()
    musicals = musicals_check.get()
    classics = classics_check.get()
    thriller = thriller_check.get()
    fantasy = fantasy_check.get()
    marvel = marvel_check.get()
    
    filters=[]
    if disney == 1:
        filters.append("disney")

    if action == 1:
        filters.append("action")

    if adventure == 1:
        filters.append("adventure")

    if comedy == 1:
        filters.append("comedy")

    if romance == 1:
        filters.append("romance")

    if horror == 1:
        filters.append("horror")
        
    if dc == 1:
        filters.append("dc")

    if chick_flicks ==1:
        filters.append("chick flick")

    if sci_fi ==1:
        filters.append("sci-fi")

    if musicals ==1:
        filters.append("musical")

    if classics ==1:
        filters.append("classic")

    if thriller ==1:
        filters.append("thriller")

    if fantasy ==1:
        filters.append("fantasy")

    if marvel == 1:
        filters.append("marvel")
    

    #This means that if the filter button is pressed but not filters are active the filters value becomes a none type
    #Allowing for the normal AI suggestion to take place
    if filters==[]:
        filters=None
        
    callback_a(list_of_films, hyperlink, film_list, user_film_choices,
               menu_title, scroll_bar, colour_schemes_button, user_details, login_username_encrypted
                                 , back_col, fore_col, button_col, scheme, watched_time_list,
                                 sign_out_button, search_entry, revert_button,
                                   filter_heading_label, disney_label, disney_button, action_label, action_button,
                                   adventure_label, adventure_button, comedy_label, comedy_button, romance_label,
                                   romance_button, horror_label, horror_button, dc_label, dc_button,
                                 chick_flicks_label, chick_flicks_button, sci_fi_label, sci_fi_button,
                                   musicals_label, musicals_button, classics_label, classics_button,
                                   thriller_label, thriller_button, fantasy_label, fantasy_button,
                                   marvel_label, marvel_button, graph_button, submit_filters, search_button, search_entry_val="", revert="", filters=filters)

    
def click1(reference_number,menu_title, list_of_films, scroll_bar, colour_schemes_button, user_details, user_film_choices, film_list, login_username_encrypted,
           back_col, fore_col, button_col, scheme, watched_time_list,
           sign_out_button, search_entry, revert_button,
           filter_heading_label, disney_label, disney_button, action_label, action_button,
           adventure_label, adventure_button, comedy_label, comedy_button, romance_label,
           romance_button, horror_label, horror_button, dc_label, dc_button,
           chick_flicks_label, chick_flicks_button, sci_fi_label, sci_fi_button,
           musicals_label, musicals_button, classics_label, classics_button,
           thriller_label, thriller_button, fantasy_label, fantasy_button,
           marvel_label, marvel_button, graph_button, submit_filters, search_button):

    #Destroys every on screen item so that the system runs at peak efficiency at all times
    list_of_films.destroy()
    scroll_bar.destroy()
    menu_title.destroy()
    colour_schemes_button.destroy()
    sign_out_button.destroy()
    search_entry.destroy()
    revert_button.destroy()
    filter_heading_label.destroy()
    disney_label.destroy()
    disney_button.destroy()
    action_label.destroy()
    action_button.destroy()
    adventure_label.destroy()
    adventure_button.destroy()
    comedy_label.destroy()
    comedy_button.destroy()
    romance_label.destroy()
    romance_button.destroy()
    horror_label.destroy()
    horror_button.destroy()
    dc_label.destroy()
    dc_button.destroy()
    chick_flicks_label.destroy()
    chick_flicks_button.destroy()
    sci_fi_label.destroy()
    sci_fi_button.destroy()
    musicals_label.destroy()
    musicals_button.destroy()
    classics_label.destroy()
    classics_button.destroy()
    thriller_label.destroy()
    thriller_button.destroy()
    fantasy_label.destroy()
    fantasy_button.destroy()
    marvel_label.destroy()
    marvel_button.destroy()
    graph_button.destroy()
    submit_filters.destroy()
    search_button.destroy()
    
    for data in range(len(film_list[int(reference_number)])):
        user_film_choices.append(film_list[int(reference_number)][data])
    
    time_data = int(film_list[int(reference_number)][2])
    
    watch_time_update(watched_time_list, time_data)
    
    main(user_details, user_film_choices, film_list, login_username_encrypted, back_col, fore_col, button_col, scheme, watched_time_list)

def callback_a(list_of_films, hyperlink, film_list, user_film_choices,
               menu_title, scroll_bar, colour_schemes_button, user_details, login_username_encrypted
                                 , back_col, fore_col, button_col, scheme, watched_time_list,
                                 sign_out_button, search_entry, revert_button,
                                   filter_heading_label, disney_label, disney_button, action_label, action_button,
                                   adventure_label, adventure_button, comedy_label, comedy_button, romance_label,
                                   romance_button, horror_label, horror_button, dc_label, dc_button,
                                 chick_flicks_label, chick_flicks_button, sci_fi_label, sci_fi_button,
                                   musicals_label, musicals_button, classics_label, classics_button,
                                   thriller_label, thriller_button, fantasy_label, fantasy_button,
                                   marvel_label, marvel_button, graph_button, submit_filters, search_button, search_entry_val=None, revert=None, filters=None): #film songs WITH hyperlinks
    
    hyperlink.reset() #ADDED THIS MYSELF TO RESET THE LIST SO THAT THEY COULD BE REFERENCED
    
    list_of_films.config(state="normal") #Sets the text box's sate to normal so items can be inserted into it and the current contents can be removed
    list_of_films.delete("1.0",END) #Removes all the contents currently in the list_of_films text box
    
########TESTING SORTING AI ALGORITHM########################################################################################################################################################

    if filters!=None:
        new_list = []
        print("THE LIST OF FILTERS", filters)

        valid=0
        for film in film_list:
            valid = 0
            for filter_trait in filters:
               # print(filter_trait,film)
                if filter_trait in film:
                    valid+=1

            if valid==len(filters):
                new_list.append(film)
        

        #SIMPLISITC AI SETUP
        #rep is a numerical representaion of how relevant the AI thinks a film is
        rep = []

        #Limits the max length of user_film_choices to 200 to make the film suggests up to date and more relevent
        while len(user_film_choices)>200:
            del user_film_choices[0] #Removes the oldest element of user_film_choices (ie the first element)
                
        for z in range(len(new_list)):
            rep.append(0)#Apends a 0 to the rep list for each film in film_list
            
        for x in range(len(user_film_choices)):#for each piece of film data stored for the user
            for y in range(len(new_list)):#for the length of the list of films
                if user_film_choices[x] in new_list[y]:#If something the user likes is in the film currently being checked
                    rep[y] = (rep[y]+1)#Add 1 to the numerical value of that film
        
        sort(new_list, rep)
        print("THIS IS REP",rep)

        hyperlink = HyperlinkManager(list_of_films, menu_title, list_of_films, scroll_bar, colour_schemes_button, user_details, user_film_choices, new_list, login_username_encrypted
                                 , back_col, fore_col, button_col, scheme, watched_time_list,
                                 sign_out_button, search_entry, revert_button,
                                   filter_heading_label, disney_label, disney_button, action_label, action_button,
                                   adventure_label, adventure_button, comedy_label, comedy_button, romance_label,
                                   romance_button, horror_label, horror_button, dc_label, dc_button,
                                 chick_flicks_label, chick_flicks_button, sci_fi_label, sci_fi_button,
                                   musicals_label, musicals_button, classics_label, classics_button,
                                   thriller_label, thriller_button, fantasy_label, fantasy_button,
                                   marvel_label, marvel_button, graph_button, submit_filters, search_button)

        for film in new_list:
            list_of_films.insert(END, film[0] + ", (" + film[1] +")", hyperlink.add(click1))
            #film[0] and film[1] ensures the user only sees the name of the film and the year of release in the text box^
            list_of_films.insert(END, "\n\n")
        list_of_films.config(state="disabled") #Sets the text box's state to disabled so it cannot be edited by the user manually

#############################################################################################
    
    if search_entry_val=="":
        search_entry=None
        
    if search_entry_val == None and filters==None:
        print("normal")
        #SIMPLISITC AI SETUP
        #rep is a numerical representaion of how relevant the AI thinks a film is
        rep = []

        #Limits the max length of user_film_choices to 200 to make the film suggests up to date and more relevent
        while len(user_film_choices)>200:
            del user_film_choices[0] #Removes the oldest element of user_film_choices (ie the first element)
                
        for z in range(len(film_list)):
            rep.append(0)#Apends a 0 to the rep list for each film in film_list
            
        for x in range(len(user_film_choices)):#for each piece of film data stored for the user
            for y in range(len(film_list)):#for the length of the list of films
                if user_film_choices[x] in film_list[y]:#If something the user likes is in the film currently being checked
                    rep[y] = (rep[y]+1)#Add 1 to the numerical value of that film
        
        sort(film_list, rep)

        for film in film_list:
            list_of_films.insert(END, film[0] + ", (" + film[1] +")", hyperlink.add(click1))
            #film[0] and film[1] ensures the user only sees the name of the film and the year of release in the text box^
            list_of_films.insert(END, "\n\n")
        list_of_films.config(state="disabled") #Sets the text box's state to disabled so it cannot be edited by the user manually

    #Creates the search system
    elif filters==None and search_entry_val==True:
        possible_searches = []
        input_split = []
        film_keywords = []

        if revert==True:
            answer = ""
        else:
            answer = search_entry.get().lower()


        input_split.append(answer.split(" ")) #Split the users answer into keywords and store them in the input_split list
        for film in range(len(film_list)): #For length of films
            #print(film_names[film])
            film_keywords.append(str(film_list[film][0].split(" ")).lower()) #split each film and store it in the film_keywords list
            
            for input_keyword in range(len(input_split[0])): #For each keyword in the users input
                if input_split[0][input_keyword] in film_keywords[film]: #If that keyword is also one of the films keywords
                    if film not in possible_searches: #And the film is not already in the possible_searches list
                            possible_searches.append(film_list[film]) #Append that film to the possible_searches list
                    else:
                        pass
                
                else:
                    pass

        print(possible_searches)
        
        comparison = []
        
        #Uses the comparison list to get a mathematical view of the amount of keywords in each possible_search
        for item in range(len(possible_searches)): #For the amount of films in possible_searches
            occurrences = 0 #Sets occurrences equal to 0
            possible_searches_title,possible_searches_date = str((possible_searches[item][:2])).split(",")
            print(possible_searches_title)
            split = possible_searches_title.split(" ") #Splits the possible searches into keywords
            for possible_search_keyword in range(len(split)): #For the amount of keywords in split
                if split[possible_search_keyword].lower() in input_split[0]:
                    #If the keyword of the possible film is also a keyword in the users input^
                    occurrences+=1 #Add one to the current value of occurrences
                else:
                    pass
            comparison.append(occurrences) #appends the current value of occurences for this item of film to the comparison list



        sort(possible_searches, comparison)

        hyperlink = HyperlinkManager(list_of_films, menu_title, list_of_films, scroll_bar, colour_schemes_button, user_details, user_film_choices, possible_searches, login_username_encrypted
                                 , back_col, fore_col, button_col, scheme, watched_time_list,
                                 sign_out_button, search_entry, revert_button,
                                   filter_heading_label, disney_label, disney_button, action_label, action_button,
                                   adventure_label, adventure_button, comedy_label, comedy_button, romance_label,
                                   romance_button, horror_label, horror_button, dc_label, dc_button,
                                 chick_flicks_label, chick_flicks_button, sci_fi_label, sci_fi_button,
                                   musicals_label, musicals_button, classics_label, classics_button,
                                   thriller_label, thriller_button, fantasy_label, fantasy_button,
                                   marvel_label, marvel_button, graph_button, submit_filters, search_button)

        for film in possible_searches:
            list_of_films.insert(END, film[0] + ", (" + film[1] +")", hyperlink.add(click1))
            list_of_films.insert(END, "\n\n")
        list_of_films.config(state="disabled") #Sets the text box's state to disabled so it cannot be edited by the user manually
        
########################################################################################################################################################################################
        

def sort(list_being_sorted, numerical_rep):
    #Sorting the list using a bubble sort where the highest value bubbles to the left#
    done = False
    while not done:
        done=True
        for index in range(len(numerical_rep)-1):
            if numerical_rep[index+1]>numerical_rep[index]:
                saved_val = numerical_rep[index+1]
                saved_film_val = list_being_sorted[index+1]
                numerical_rep[index+1]=numerical_rep[index]
                list_being_sorted[index+1]=list_being_sorted[index]
                numerical_rep[index]=saved_val
                list_being_sorted[index]=saved_film_val
                done=False
                
    print(numerical_rep)


def graphing(watch_time_list): #Function used to test if the graphs button works
    x = [1,2,3,4,5] #X co-ords
    my_xticks = [] #X axis increments
    y = [] #Y co-ords
    for data in range(len(watch_time_list)):#For the length of the watch_time_list
        watch_time_value, date_stored = watch_time_list[data].strip().split(" ", 2)#Split the stripped list to get the value and the date seperately
        d = datetime.strptime(date_stored,'%Y-%m-%d') #Gets old format year - month - day
        new_d = d.strftime('%d-%m-%Y') #Converts format to day - month -year
        my_xticks.append(new_d)#Appends the stored date to the dates list
        y.append(int(watch_time_value))
        
    plt.rcParams["axes.facecolor"] = "black" #Manually sets the background color to black
    plt.rcParams["toolbar"] = "None" #Removes the toolbar
    #tick_spacing = 1 #Y axis spacing
    fig, ax = plt.subplots(1,1)
    plt.xticks(x, my_xticks) #Plot ticks
    plt.ylabel("Watch time")
    ax.plot(x,y, "gold") #Plot a graphs of x against y and make the line gold
    ##ax.yaxis.set_major_locator(plttick.MultipleLocator(tick_spacing)) #Sets the tick spacing
    plt.show() #Display the graph

opening()
