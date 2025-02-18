# JobAppBot

## General information
Try to edit and test in small units, that way you dont need to have the whole application running. 
Currently, there is a docker container that can be started with the **docker up** command. However, this approach proved to be a bit problematic when trying to access external APIs. Going to resort back to having both running locally on a Flask server for the python backend and something else for the frontend, still need to do research. 

Testing and editing in units helps us bypass this issue and just test locally. For example, when testing a specific function, run it in the terminal to validate if it works, rather than booting the whole application. It also helps us break this into smaller bits to then fit together later (woohoo abstraction). If you are making an API endpoint, you can verify that it works by using software such as postman or using the curl command in your terminal. 
