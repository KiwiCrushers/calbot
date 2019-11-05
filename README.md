# calbot

![](https://github.com/KiwiCrushers/calbot/blob/master/logo/cover.png)

## HackFSU6 First Place Winner
***Calbot is currently in Pre-Alpha. If you encounter any issues, please don't hesitate to open an issue. Thanks for helping on this journey!***
 
## Inspiration 
In a world where 2/3 of the US population is considered overweight, it has become increasingly important to track and control our nutritional intake. In that manner, there is a lack of technologies such as machine learning being applied to solve this increasingly severe population epidemic. We wanted to make a product that would encourage responsible eating habits by making it easy and rewarding to keep track of your intake using the latest and greatest in Machine Learning technology. We wanted to make it easier than ever to stay healthy with a model that can be used by people of all different kinds.
## What it does
CalBot tracks your food intake by processing simple snapshots of your food and classifying it using the latest in machine learning thanks to Google Cloud Vision AI Object Detection. All you have to do is take a picture, and CalBot will sort and identify the nutrition information of that food and keep track of it for that day.
## How we built it
We built a cross-platform API for CalBot, allowing us to implement the service both in popular messaging platforms like Discord as well as a modular native interface. Beneath the surface, CalBot runs in Python, employing the Google Cloud Vision AI to recognize images in real time as well as on the Wolfram Informational Database to provide advanced nutrition information. Then, the service is deployed to popular messaging platforms through their respective API's, as well as through the native client, built in-house on a Flask web server to provide flexibility and ease of access. Additionally, Version Control was executed throughout the team using Git and GitHub. Moreover, documentation and a product showcase page were developed and are hosted on GitHub Pages.  
## Challenges we ran into
The biggest challenge that the team ran into was developing the native interface because of its independence from bulky web building platforms. Furthermore, there was a significant learning curve in developing comparability and functionality with the Google Cloud ecosystem of products. Furthermore, there were outstanding technical limitations as Machine Learning is very much still a developing field.
## Accomplishments that we're proud of
In less than 24 hours, we built an entirely native intelligent chatting interface alongside our ports to popular messaging clients such as Discord and Slack. Our resulting ecosystem is extremely accurate and can identify both ingredients, foods, and brand name packaged perishables.
## What we learned
Throughout this experience, we learned efficient use of the Google Cloud suite of products, advanced version control with several team members, and basic natural language processing in order to parse the necessary commands for CalBot to operate efficiently. 
## What's next for CalBot
We plan to release our technology in an open source fashion to allow for the developer community to enhance CalBot and use its technologies for the general improvement of the general population health. And to begin tackling one of the most troubling population threats in the United States.
