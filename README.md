# final_assignment
 
This python script extracts the useful data from 3 different datasets, which could be found on:

-https://www.kaggle.com/sudalairajkumar/daily-temperature-of-major-cities

-https://data.overheid.nl/dataset/802-visserij-en-aquacultuur--hoeveelheid-vis--schaal--en-schelpdieren#panel-resources

-https://data.overheid.nl/dataset/803-visserij-en-aquacultuur--prijzen-verse-vis--schaal--en-schelpdieren#panel-resources

-https://data.europa.eu/data/datasets?categories=agri&page=2&locale=en&format=CSV&query=fishery

The script extracts the shrimp catch prices and catch rates per year and merges it with data from other countries, together with the temperature of the selected countries, to search if there is any correlation between catch rates and temperatures.

The script outputs plots, which show shrimp prices per kg over time(years) and also shows a line, which is the average inflation per year.

## room for improvement:
this script could be improved a lot, it was first progammed in a main file without using functions, after which the code was put into functions. this is visible in the way, that the program does not seem to be object oriented programmed. also, the structure of the script could be way better and using a uniformal styling (PEP8) is needed. aside from this, lots of dataframes are made, which is not nessecary, this could be done more efficient. also, the entire code is not optimized for speed, which could also enhanced a lot.

### it is important to use main2, since main branch got broken because of a too big file in the history
