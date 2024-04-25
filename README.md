# pub-lish
Human interface project




Need to keep static files such as images and the CSS stylesheet in the static folder in order for Flask to render it
TO IMPORT A FILE/IMAGE/STYLESHEET/URL INTO HTML YOU HAVE TO DO IT LIKE {{url_for('static', filename='style.css')}} DO NOT DO <link rel="stylesheet" href="style.css"> ITS NOT GOING TO FUCKING WORK
TEST THIS SHIT USING
 flask --app publish.py --debug 
SO YOU CAN ACTUALLY SEE IT WORK HOW ITS SUPPOSED TO


Templates store all of the html pages
Publish.py is the backend

To use on your machine 
    pip install Flask
    pip3 install mongita
    python create_db.py
    flask --app publish run