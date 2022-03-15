# Instructions

## Button Auto-Border & Gradient.py
Please download the corresponding ZIP [here](https://drive.google.com/file/d/11_kogySoJkuKgoBxbaKfW9Lh9SiuK95C/view?usp=sharing)
_This script will create a backup of all affected files as it runs. Please make sure to make a copy of the original folder if you are still concerned._

The whole purpose of this script is to make those pretty buttons with the borders and gradients extremely simple to do. To prepare for using this script, you'll want to do the following:
- Create the `[charactername]\emotions` folder ahead-of-time
- Have all your emotion buttons be 38x38 with a canvas size of 40x40
    - If I just made 0 sense, grab the XBS script from the ZIP and use it to run your buttons through XnConvert first.
- Have "border.png" in the same folder as your buttons
- Optional: Have "gradient.png" in the same folder as your buttons

So by now, you're going to have something like this
![image](https://user-images.githubusercontent.com/27789584/158398840-61411f90-a3dd-41c3-9644-cf41a37fbae1.png)

Now, you just run the script, and ta-da: You have bordered buttons w/ your gradient background!

![image](https://user-images.githubusercontent.com/27789584/158398892-1a0b0291-b034-40ec-9710-4c986d258f4d.png)
Before                     |  After
:-------------------------:|:-------------------------:
![button1_off](https://user-images.githubusercontent.com/27789584/158399392-f8812146-660c-48ee-96d2-2c0e1bffd998.png)|![button1_off](https://user-images.githubusercontent.com/27789584/158398976-efaafcf7-3fa4-4ea7-85e9-146ee33fe1de.png)


IF THE SCRIPT DOESN'T WORK: OPEN YOUR COMMAND PROMPT AND RUN IT FROM THERE. IF IT SAYS THERE IS NO MODULE NAMED "PIL", RUN `pip install Pillow` - THIS *SHOULD* FIX THE ISSUE.
