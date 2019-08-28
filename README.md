# pyster
An automatic poster tailored for a specific forum using pyautogui

## Disclaimer

The script is a custom solution a friend has asked for me in order to post automatic messages on a particular online community. He pledged that he would be using the tool in a non-agressive way with a 14-day interval between any message to a specific user. I trust his word that he won't abuse Pyster. 

Anyone wanting to use it for oneself first has to adapt the script to one's particular needs. If one chooses to abuse the script in order to spam other people, it is one's sole responsibility.

## Description

The script:
- captures specific coordinates on the user's screen in order to navigate the forum 
- scrapes a given number of account names from the forum, verifying that the accounts have not been contacted in the last fortnight ;
- messages each user from the dict with the provided message. 

All interaction with the forum is made through the user's browser, once the user has logged into the forum and filtered the forum accounts according to his needs.

## Contributions

Are always welcome! The whole purpose of this script, apart from solving a real-world prolem, is for me to learn some efficient, pythonic coding. It is probably full of programming childhood diseases. Some to-do's I've already identified are:

- read PEP8 **once again** and check the whole script carefully
- scrape a list first, clean it, and pass to a dict only after messaging people

## License
MIT
