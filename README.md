# Myntra-Hackerramp-2021-WeForShe

### Problem Statement: Lack Of Senior Citizens’ Engagement On Online Fashion Platforms

### Theme:  Customer Delight

## Project Description:

### Context:

Given our vision of "INTERNET FOR ALL", it is a source of prime concern that people above
45 years of age (of course, the richer one) form only 10% of 45.6 million online shoppers
in India. In a study by telenor, it was found that out of the remaining 90% who do not
shop  online, 24% say that Internet is too "complicated" for them. Talking specifically 
about fashion industry, major problem lies in:<br>
1)The trends shown on the platform are probably based on kids, and 20-45 years age groups of people, and also not region wise.<br>
2)Based on clothing showcased on young aged models on the platform they are probably not able to decide whether it will suit their needs or not.<br>
3)Overflow of information without proper help<br>

### Solution
So, we have come up to a solution of senior-centric fashion platform "FOSTERS" majorly comprising of:<br>
1)Fetching of age and location at the time of registration<br>
2)Seperate section for "SENIORS" for hassle-free search<br>
3)Region-wise recommendation of clothes i.e. North,South,North-East,Western etc.<br>
4)Voice assistant for navigation of the website<br>

### Instructions for project set up

Step 1: Fork a copy of the project. 
 git clone https://github.com/mansimaurya19/Myntra_Hackathon.git <br>
Step 2: Install dependencies.
   pip install -r requirements.txt<br>
Step 3: Run app.py.Now,you are good to go<br>

 
 ### Implementation
 
 1)We have created the dataset of clothes region wise by scrapping the traditional clothes worn more often in a particular state. Then, metadata for images was created containing the title of the image, image id, and labels being the region namely South, North, North-East & Western.
<br>

2)The image collected are classified using open-cv library and rendered to the user using flask requests in backend. Based on the region input he/she gives, different images are recommended to the user from our database.
<br>

3)We have provided a voice assistance  feature in our prototype  that will help the user to navigate through the website easily.For an instance,if the  user gets stuck somewhere on any page, then they can simply click on the microphone button provided in the navbar and say “Redirect to Home Page“ or “Go to Home Page".
<br> Webkit Speech Recognition library to detect the voice from our frontend(user) and give it our backend in text form using splits and tokens<br> 
 

 
<br>

### If you were not able to run the project, don't worry we have got a Demo Video for you:
Link: <a href="https://drive.google.com/file/d/1FBGsaHq_WMNg2AvCFUIs2IXeCgfaTr8X/view">demo video of our project</a>

<br>



## Demo images
<p align="center">
<img src ="https://github.com/mansimaurya19/Myntra_Hackathon/blob/master/demo-images/Screenshot%20(1220).png" height="500"/><br>
 <br>
<img src ="https://github.com/mansimaurya19/Myntra_Hackathon/blob/master/demo-images/Screenshot%20(1221).png" height="500"/><br>
 <br>
<img src ="https://github.com/mansimaurya19/Myntra_Hackathon/blob/master/demo-images/Screenshot%20(1222).png" height="500"/><br>
<br>
<img src ="https://github.com/mansimaurya19/Myntra_Hackathon/blob/master/demo-images/Screenshot%20(1223).png" height="500"/><br>
<br>
<img src ="https://github.com/mansimaurya19/Myntra_Hackathon/blob/master/demo-images/Screenshot%20(1224).png" height="500"/><br>
<br>
<img src ="https://github.com/mansimaurya19/Myntra_Hackathon/blob/master/demo-images/Screenshot%20(1225).png" height="500"/><br>
                                                                                                                        </p>
<br>



### Future scope:

In future, we are planning to improve our database for more holistic recommendations and extend cross-platform
demonstration with native language support.







