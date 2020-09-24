from colorama import Fore, init, Style
import threading, requests, os

init(convert = True)

os.system("title Shoppy Seller Finder!")

while True:
	word = requests.get('https://random-word-api.herokuapp.com/word?number=1').text.split('["')[1].split('"]')[0]#this api is fun af hehe - returns a word upon request :)
	a = requests.get(f"https://shoppy.gg/api/v1/public/seller/{word}")
	if str(a.status_code) == "200": #shh 
		print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}https://shoppy.gg/@{word}")
		f = open("taken.txt", "a") #this is for if your tryna find sellers
		f.write("https://shoppy.gg/@" + word + "\n") # f strings messing up allow it
		f.close()
		os.system(f"title Checked shoppy.gg/@{word} - Taken ")
	elif str(a.status_code) == "422": #shh 
		print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}]{Fore.RED} https://shoppy.gg/@{word}")
		f = open("untaken.txt", "a")#this is for if your tryna find fancy names
		f.write("https://shoppy.gg/@" + word + "\n") # f strings messing up allow it
		f.close()
		os.system(f"title Checked shoppy.gg/@{word} - Untaken ")
	else:
		if str(a.status_code) == "200": #kept on saying sum after finding valids - this makes sure its not status code 200 
			pass # Stuffs being playing up - couldn't do ! if not method but will try next time :flushed:
		else:
			print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.RED}Error - Most likely Ratelimitted.")
			os.system(f"title Error occured.")
#api doesn't have much details on it but might make one that detects products one day , who knows :) - show some support by leaving a star.
#Might also allow the loading of usernames, but this was a tool I made for the purpose of finding suppliers so ya

