Sahal Shaikh




I used python3 for this project

#############
How to run

It can be run by

   python3 portal.py arg1 arg2 arg3 .....

   for example if you want to run AddUser
       python3 portal.py AddUser user password

#######
Some additional information

-> I have used six different files to store data and all of the files will be saved under a subdirectory called portal_data.
-> No need to do any set up, I have handeled everything in the program. It will create subdirectory and requred files autometically when you run the programm.


##################
Example test scripts

-> i have used bash script to test the program.

* Tried to add 500 users.
  Bash Script

       for i in {1..500};do python3 portal.py AddUser user-$i password-$i;done

* Authenticate 500 users.
  Bash Script

       for i in {1..500};do python3 portal.py Authenticate user-$i password-$i;done

       Test for bad password (ERROR)
       for i in {1..500};do python3 portal.py Authenticate user-$i password;done



* Set Domain
  set 1 to 100 users as admin

      for i in {1..100};do python3 portal.py SetDomain user-$i admin;done

  set 100 to 200 users as premium-subscriber

      for i in {100..200};do python3 portal.py SetDomain user-$i premium-subscriber;done

  set 200 to 300 users as editor

      for i in {200..300};do python3 portal.py SetDomain user-$i editor;done

  set 1 to 500 users as normal-subscriber

      for i in {1..500};do python3 portal.py SetDomain user-$i normal-subscriber;done


* Domain Info

  check domain information

  	python3 portal.py DomainInfo admin
	python3 portal.py DomainInfo editor
	python3 portal.py DomainInfo normal-subscriber
	python3 portal.py DomainInfo premium-subscriber

* Set Type

  setting 1 to 300 music#.mp3 to music

  	  for i in {1..300};do python3 portal.py SetType music-$i.mp3 music;done

  Setting 100 to 500 audio-#.mp3 to music and audio
  
  	  for i in {100..300};do python3 portal.py SetType audio-$i.mp3 music;done
	  for i in {100..300};do python3 portal.py SetType audio-$i.mp3 audio;done

  Setting 1 to 300 videos

  	  for i in {1..300};do python3 portal.py SetType video-$i.mp4 video;done

  Setting 300 to 500 movies
  	  for i in {300..500};do python3 portal.py SetType movie-$i.mp4 movie;done


* Type Info
  Check type information

  	python3 portal.py TypeInfo movie
	python3	portal.py TypeInfo video
	python3	portal.py TypeInfo music
	python3	portal.py TypeInfo audio


* Add Access

      python3 portal.py AddAccess view premium-subscriber movie
      python3 portal.py	AddAccess view normal-subscriber video
      python3 portal.py	AddAccess edit editor video
      python3 portal.py AddAccess edit editor audio
      python3 portal.py AddAccess download admin music
      python3 portal.py AddAccess download editor video


* Can Access

  check if user have access

  	# Half Success and Half AccessDenied 
  	for i in {1..300};do python3 portal.py CanAccess download user-$i music-$i.mp3;done

	# Access denied 
	for i in {100..200};do python3 portal.py CanAccess view user-$i movie-$i.mp4;done

	# Only first one Success and others Access Denied 
	for i in {300..500};do python3 portal.py CanAccess view user-$i video-$i.mp4;done

	# Success 
	for i in {200..300};do python3 portal.py CanAccess edit user-$i video-$i.mp4;done

