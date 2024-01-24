# website-for-band

For this project i use django, python, css and html.

This website only shows the information for the website to the user's who has an account and if you don't have an account yet, it allows you to sign up and then login to view the information on the website.

This website have three pages only, which is home page, about page and events page.

When you login to view the website info it takes you to the home page where it guides you on what to do. Like for example it tells you if you want to know about us, please visit our about page and for the upcoming events, please visit our events page.

The about page tells you all the information you need to know about the band and their band members with their roles.

The events page shows you the information for the upcoming events along with the dates of the events.

If you want to install this webpage and use it, please download all the files that i have provided and follow these steps to make your webpage run without errors :

 1. When you are done downloading this web page, please put the files into one folder called band

 2. Open your code editor and open the folder that you have created called band

 3. After opening the folder called band with all the files that you have downloaded in it, open the terminal.

 4. After opening the terminal, you must run this command to install all the requirements that are needed for this website
    : pip install requirements.txt

 5. When it's done installing requirements.txt, you have to nevigate to file called webpage. you can nevigate to this 
    folder by running this command : cd webpage 

    Make sure that you have installed django in this app, if you are not sure whether you have it or not then run
    this command to install django : pip install django

 6. Before we continue please delete the data base first called db.sqlite3 so that you can create your own database.

 7. After deleting this data base, please input this command in your terminal : python manage.py makemigrations
    then python manage.py migrate

 8. Then input this command that is going to allow you to login to admin page : python manage.py createsuperuser.
    This command is going to ask you to input the username, email, password and the confirm password.

 9. After doing this please run this command so that you will be able to open your local host or server :
    python manage.py runserver

 10. Follow/open the link that will be displayed on the output, For example: http://127.0.0.1:
 
 11. when you open this link it will take you to the website and on the website it will show you some errors like it
     it was not found so in order to fix these errors you have to input what the website have provided for you on the webpage, like the urls from your code. 

 12. At the end of the local host put admin to go to admin page, For example: http://127.0.0.1:/admin then press
     enter and if you you want to go to band website input this For example: http://127.0.0.1:/band then press enter

After doing all these steps the website will be working without any errors
