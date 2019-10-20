import requests, json, sqlite3, datetime
import Mods.calories as calories
import Mods.vision as vision

with open("json/config.json") as h:
    config = json.load(h)

calories = calories.Client(config["wolfram"]["app_id"])

def calories_from_url(url, userId, attachmentId):
    # Retrieve the filetype of the URL.
    filetype = url[-3:]

    # Downloading the file into our system.
    r = requests.get(url, allow_redirects=True)
    filePath = 'images/' + str(userId) + '-' + str(attachmentId) + '.' + str(filetype)
    open(filePath, "wb").write(r.content)

    # Calculating the amount of calories.
    foodData = calculate(filePath)
    # Adding the entry into our database.
    conn = sqlite3.connect("db/database.db")
    c = conn.cursor()
    c.execute("INSERT INTO meals VALUES ('"
    + datetime.datetime.now().isoformat() + "','"
    + str(userId) + "','" + foodData["name"] + "','" + str(foodData["calories"])
    + "');")
    conn.commit()
    conn.close()
    return foodData
    

def calculate(filePath):
    totalCals = 0
    # Getting the labels from Vision.
    for label in vision.detect_labels(filePath):
        label = label.description.lower()
        if check_food_for(label):
            print("Food: " + label)
            # If the object is a valid food.
            cals = calories.calCount(label)
            print("Calories: " + cals)
            return {"name": label, "calories": cals}


def check_food_for(item):
	food = open("FOOD.txt").readlines()
	for index, string in enumerate(food):
		if item == string[0:-1]:
			return True
	return False