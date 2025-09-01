# **Interactive Clock & Tools**

This is a Python project that combines an **interactive clock** with additional tools like a **timer, stopwatch, world clock**, and a **rock-paper-scissors game**. The program also detects your **current country** using your IP.

## **Technologies Used**
- **Python 3**  
- **Requests** library to get user location  
- **Pytz** for timezone handling  
- **Difflib** for fuzzy matching of timezones  
- **Random** for game interactions  
- **Datetime** for date and time operations  

## **Features**
- **Displays current time** in your local timezone  
- **Shows your country** based on IP  
- **Timer** with countdown  
- **Stopwatch** with second-by-second display  
- **World clock** to show time in any city  
- **Rock-paper-scissors game** as a fun extra  

## **How to Run**
1. Clone this repository:  
`git clone https://github.com/mateus-alarcao/interactive-clock.git`  
2. Make sure you have Python installed.  
3. Install required libraries:  
`pip install requests pytz`  
4. Run the script:  
`python clock.py`  

## **Usage**
- Follow the menu to choose an option:  
  1. **Timer** – enter seconds for countdown  
  2. **Stopwatch** – count seconds incrementally  
  3. **World Clock** – enter a city or location to see its current time  
  4. **Exit** – close the program  
  5. **Extra** – play a rock-paper-scissors game  
