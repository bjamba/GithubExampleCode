# GithubExampleCode
This is a portfolio of example projects that I've created while studying at the Tech Academy in 2017.  They include, but are not limited to:

# 1. JobBoardScraper
A web scraper developed in C# to obtain job postings from a website and post to an Azure DB server from a local computer. I developed this as part of my two-week Live Project course at the Tech Academy in May 2017, as part of a non-commercial job board website our Scrum team was continuing to develop. My predecessors originally developed a scraper in Python but had compatibility issues with posting the data to Azure.  Their original workaround was to output to a JSON file, then manually update the DB with the data from those JSON files.

I was tasked to built a new C# scraper from scratch, since the website itself was an MVC project with C# classes for the job postings. I included a scheduler to allow for it to run in the background at set intervals to avoid the need for manual scrapes, and provided the option to output a JSON file to a local computer, in case that was every needed for future development purposes.  My solution was also organized so that we could simply add a new .cs file with minimal new code for each company website we added to the scraper.  However, because the code behind the scheduler and the uploading of the job postings did not need customization for each website, I segregated those parts of the code and made them callable methods instead.

Note:  I also created a dummy DB server on Azure purely for development purposes, and so it does not impact any live Azure server.  The credentials included are meant only to test its functionality to a live server (as opposed to using localDB or a similar local solution).  A firewall exception needs to be added for the IP address of the specific local computer, if you want to test this code.  Please contact me if you would like me to add a firewall exception to you, using the contact information on my applications materials.

# 2. Grandma's Birthday Cash Game
This is a program created in Python that is a short, funny little text adventure game where it takes input information (name, age, etc.) to roleplay the childhood memory of receiving birthday cash from your grandma.

# 3. Batch Filemover
This is a program created in Python that allows for the batch moving of files from one folder on your computer to another, done with a GUI using Tkinter.
