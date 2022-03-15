# Instructions

## Button Auto-Border & Gradient.py
Please download the corresponding ZIP [here](https://drive.google.com/file/d/11_kogySoJkuKgoBxbaKfW9Lh9SiuK95C/view?usp=sharing)
_This script will create a backup of all affected files as it runs. Please make sure to make a copy of the original folder if you are still concerned._

The whole purpose of this script is to make those pretty buttons with the borders and gradients extremely simple to do. To prepare for using this script, you'll want to do the following:
- _Make sure to have Python 3.8 (earliest tested version), should work on most Python 3.x versions however._
- Create the `[charactername]\emotions` folder (if you haven't already)
- Have all your emotion `buttons` in the folder.
- Have `border.png` in the same folder as your buttons. Must be the same size as the buttons
- Optional: Have `gradient.png` in the same folder as your buttons (this adds a background layer to the image), must be the same canvas size as the buttons
- Run the script. (You won't get a prompt saying success/fail if you double-click the file. If it is not running, open Command Prompt and run it from there - It's possible that the script is trying to tell you something, but since it auto-closes you can't see it!)

So by now, you're going to have something like this
![image](https://user-images.githubusercontent.com/27789584/158398840-61411f90-a3dd-41c3-9644-cf41a37fbae1.png)

Now, you just run the script, and ta-da: You have bordered buttons w/ your gradient background!

![image](https://user-images.githubusercontent.com/27789584/158398892-1a0b0291-b034-40ec-9710-4c986d258f4d.png)
Before                     |  After
:-------------------------:|:-------------------------:
![button1_off](https://user-images.githubusercontent.com/27789584/158399392-f8812146-660c-48ee-96d2-2c0e1bffd998.png)|![button1_off](https://user-images.githubusercontent.com/27789584/158398976-efaafcf7-3fa4-4ea7-85e9-146ee33fe1de.png)


IF THE SCRIPT DOESN'T WORK: OPEN YOUR COMMAND PROMPT AND RUN IT FROM THERE. IF IT SAYS THERE IS NO MODULE NAMED "PIL", RUN `pip install Pillow` - THIS *SHOULD* FIX THE ISSUE.
