mkdir Projects

cd Projects

mkdir Version-1 Version-2 # creates our directories

cd Version-1 # moves us into the home directory

touch index.html index-2.html contact-us.html services.html services-2.html abous-us.html # creates all our files

mv index-2.html services-2.html ../Version-2 # since we're in our Version-1 folder, we need to tell our computer to grab our files, move OUT THEN INTO another directory Version-2

cd ../.. # this moves us back to home directory cli-activity

mv Projects/Version-2/index-2.html Projects/Version-2/services-2.html Projects/Version-1 # Since we're in our home directorym we need to provide our relative path for the files we need to move, AND the relative path for where we want them 