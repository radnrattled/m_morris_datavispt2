#Olympic Gold Medal Data Vis Part 2

##Thesis: 

Since their induction into the Winter Olympics in 1924, Women eventually grow to win more gold medals than men 

##Data analysis 

Year 		Golds for Men		Golds for Women

1924			9			0
1928 			12			0
1932			14			0
1948			17			1
1952			16			0
1960			1			2
1964			4			0
1968			1			1
1976			0			0
1984			2			0
1992			0			5
1994			1			2
1998			7			7
2002			30			33
2006			6			23
2010			41			27
2014			32			31

Totals:           Men=193 	Women= 132
1924-1952 -  Men=68		Women= 1
1960-1984 -  Men=8 		Women= 3
1992-2014 -  Men=117 	Women= 128

##Road Map: 

Pie Charts because I am comparing two variables
I want to first create a pie chart to compare the total number of golds between men and women between 1924 and 2014

Then want to break down the time line into 3 pie charts 1924-1952, 1960-1984 and 1992-2014. These charts will clearly show the change in majority of gold won among the genders as women gain more rights and participate in more sports. 

##Road map to pie charts: 

import matplotlib.pyplot as plt

Medals = (x,x)
gender = ['Men', 'Woman']
colors = ['r', 'g']

plt.pie(Medals, labels=gender, colors=colors, startangle=90, autopct='%.1f%%')
plt.show()

##Prerequisites: all you need is an updated Google Chrome, Mozilla Firefox or Safari browser

##To view app: Clone the project, cd to your directory/ download and run the index.html file in an updated Google Chrome, Mozilla Firefox or Safari browser.

##Built with Python 3


