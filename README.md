# Vaccine Slot Availability Checker

Tired of refreshing the cowin website page again and again to check whether vaccination slot is available for you or not? 
Here's the solution. Use this app to get a notification on the pc it is running in as well as a WhatsApp message too so you don't need to sit in front of your screen.

<h2>Instructions:</h2>
<ul>
<li> Edit the inputs.py file according to your requirements. 
<li> Set the pincode, age and time interval.
<li> Ensure that your system has Python 3.6+ installed and is added to PATH. 
<li> Run "pip install -r requirements.txt" in cmd to install required modules in your system.
<li> You will need chrome webdriver for this app to work. You can download it easily from https://chromedriver.chromium.org/downloads according to the chrome version you are using. 
<li> As you start the app.py file, it'll launch a new chrome window where you need to scan the QR for Whatsapp web. After scanning the QR, press Enter key in console.
<li> Sit back and let it do it's work.
<li> If the slot is available, it'll make a beep sound as well as send a WhatsApp message to the contact that you specify.</ul>

<h2>Recommendations</h2>
<ul>
  <li> Do not set the threshold time below 30 seconds so as to avoid DoS.
  <li> Change the inputs.py file according to instructions written below each variable
  <li> If you do not want WhatsApp feature, comment out the following lines in app.py: <ul> <li> 8<li> 9<li> 11-14<li> 30-32<li> 35<li> 37</ul></ul>
  
<h2> Note </h2>
This app or me has nothing to do with your WhatsApp data. All the processes are happening on your local machine.

<h2> Why is this app better than other websites available on the internet </h2>
Since it is running on your local PC handling only your requests rather than handling hundreds and thousands of requests, there are almost 0 chances of DoS (Denial of Service) from the CoWIN server and that increases the accuracy. The only drawback is thay you will need to keep your PC on.


<br><br>
<H4>Suggestions are always welcome
