musician_list = ["Bump", "Spitz", "Raswinps", "Mr.Children"]
locations =[(23.4, 432.5), (5002, 234.4)]
mydict = {"height": 166, "weight": 60, "country": "Japan"}

def get_info():
	print("What do you want to know?")
	key = input()
	print(mydict[key])

music_box = {"Bump": ["Ramp", "Laugh Maker", "K"],
             "Spitz": ["Song of Spring", "Cherry", "Lookn' for"]}

get_info()