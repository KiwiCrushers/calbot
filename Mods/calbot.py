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
    query = ("INSERT INTO meals VALUES ('"
    + datetime.datetime.now().isoformat() + "','"
    + str(userId) + "','" + foodData["name"] + "','" + str(foodData["calories"]) + "''" + str(foodData["caffeine"])
    + "');")
    c.execute(query)
    conn.commit()
    conn.close()
    return foodData
    
def food_today(userId):
    conn = sqlite3.connect("db/database.db")
    c = conn.cursor()
    query = "SELECT * FROM meals WHERE userId='" + str(userId) + "';"
    c.execute(query)
    allFood = c.fetchall()
    totalCals = 0
	totalCaf = 0
    todayMeals = []
    for meal in allFood:
		#iterate over all food, and make a table of food eaten today
        mealDate = datetime.datetime.strptime(meal[0], "%Y-%m-%dT%H:%M:%S.%f")
        if(datetime.datetime.date(mealDate) == datetime.datetime.date(datetime.datetime.today())):
            todayMeals.append(meal)
	#iterate over all food eaten today and sum calorie + caffeine counts
	for meal in todayMeals:
		if isinstance(meal[3], int):
			totalCals += meal[3]
		if isinstance(meal[4], int):
			totalCaf += meal[4]
    return {"list": todayMeals, "total": totalCals, "caffeine": totalCaf}

def calculate(filePath):
    totalCals = 0
    # Getting the labels from Vision.
    labels = vision.detect_labels(filePath)
    for label in labels:
        label = label.description.lower()
        if check_food_for(label):
            print("Food: " + label)
            # If the object is a valid food.
            cals = calories.calCount(label)
            if cals != "No calorie data.":
				caf = calories.cafCount(label)
                print("Calories: " + str(cals))
				print("Caffeine: " + str(caf))
				return {"name": label, "calories": cals, "caffeine": caf}
    return {"name": "Cannot Recognize Food.", "calories": "No calorie data.", "caffeine": "No caffeine data."}


def check_food_for(item):
	food = open("FOOD.txt").readlines()
	for index, string in enumerate(food):
		if item == string[0:-1]:
			return True
	return False