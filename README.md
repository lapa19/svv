# svv
Search engine vector voting

SVV is a meta search engine[1] which collects results from 4 search engines- AOL, Ask, Bing, Yahoo for a given query and displays to user. It uses the concept of On the fly document clustering (OTFDC)[2] to give more relevant search results.
It also displays the vote distribution of a particular search result among the search engines and relevance for each result and the rank of the particular web document in each of the search engines. 

To run the search engine on localhost, the following need to be installed-

1. BeautifulSoup (Python Library)

2. MySQLdb (Python Library)

3. Multiprocessing (Python Library)

4. Urllib (Python Library)

5. MySQL, Apache server (Xampp most convenient)

To run the search engine, paste the files in the appropriate location on your system and run it like any normal php file on browser. Enter query in the search bar. The results will be displayed in approximately 10s.

This was implemented as part of an academic project for the course Web Technology and Applications. 
The referred research papers for the implementation were: 

[1] http://www.emeraldinsight.com/doi/abs/10.1108/10662240510615182 (SVV)

[2] http://www.sciencedirect.com/science/article/pii/S0306457310000373 (OTFDC)

Screenshot of Output for the query "APJ Abdul Kalam":
![Screenshot of output](/Screenshot from 2016-11-06 18_02_08.png?raw=true "screenshot1")
![Screenshot of output](https://raw.githubusercontent.com/lapa19/svv/master/Screenshot from 2016-11-06 18_02_08.png)

