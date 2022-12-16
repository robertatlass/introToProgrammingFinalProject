# Rock Paper Scissors X Chrome Extensions

ARE YOU ADDICTED TO ROCK PAPER SCISSORS.... THIS GAME IS FOR YOU! UNLIMTED ROUNDS OF ROCK PAPER SCISSORS EVEN IF YOU HAVE NO FRIENDS!

## Description
My Chrome extension is a rock paper scissors game. In this game the player inputs their choice of: "rock, paper, or scisscors." 
Then the computer picks from "rock, paper, or scisscors," at this point the computer and player choices are evaluated through 
a series of if statements. After the evaluation the winner is determined and the appropriate message is printed. If the user is defeated they must wave the white flag of defeat, via written admission of deafeat in order to end the game.

The rock paper scissors game is written in Python and because it is packaged as a chrome extension the program utlizes a Transpiler called Brython (stands for Browser-Python BTW). The Brython Transpiler takes the code that the user pastes into the terminal in the Chrome Extension and changes it to a web acceptable format (Java Script). 

## Getting Started

### Dependencies
This game has a few main dependencies.

- Dependency 1: Must have python installed 
- Dependency 2: Must have acces to the random library
- Dependency 3: Rock Paper scissors icon
- Dependecy 4: Brython
- Dependency 5: Google Chrome

### Installing
There is a multi step installation procces to get this running correctlly:

- Step 1: Create a new folder on your local machine titled "Rock_Paper_Scissors Chrome Extension"
- Step 2: Navigate to the folder titled "Learning The Extension" in this repository
- Step 3: Download these files in the "Learning The Extension" folder and save them to your "Rock_Paper_Scissors Chrome Extension" on your local device (It is important you do not rename any of these files):
               - RPS.PNG
               - Main.py
               - manifest.json
               - popup.html
               - popup.py
- Step 5: Open Google Chrome and enter the URL: chrome://extensions/
- Step 6: Turn on "Developer Mode" in the upper right hand corner of the screen and then click "Load Unpacked" in the upper left corner
- Step 7: Select the "Rock_Paper_Scissors Chrome Extension" folder on your local device and unpack this folder

These are all the installations steps. If you have any installation questions the https://developer.chrome.com/docs/extensions/ has thorough and straightforward installation resources.

### Executing program

The program will run when you click the icon in the top right of the screen
One you click on the program you will be prompted to click any button on your comptuer to begin the game.

THe game utilizes the keys W,A,S,D to ove the charecter and spacebar to jump.

## Help
- Uninstall and reinstall the program
## Authors

Contributors names and contact info

Robert Atlass
Robert.atass23@bcp.org

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [w3Schools](https://www.w3schools.com/python/default.asp)
* [PyGame](https://www.pygame.org/docs/)
* [Automate The Boring Stuff](https://automatetheboringstuff.com/)
* [Chrome_Dev_Page](https://developer.chrome.com/docs/extensions/mv3/)
* https://www.youtube.com/watch?v=0n809nd4Zu4
* https://www.youtube.com/watch?v=uV4L-wcnK3Y
* https://support.google.com/chrome/a/answer/2714278?hl=en
* https://developer.chrome.com/docs/extensions/mv3/getstarted/extensions-101/#building
* https://pythonspot.com/create-a-chrome-plugin-with-python/
* https://www.reddit.com/r/learnpython/comments/oi6wk8/creating_a_chrome_extension_with_python/
* https://realpython.com/brython-python-in-browser/#creating-google-chrome-extensions
* https://www.extension.ninja/blog/post/solved-permission-is-unknown-or-url-pattern-is-malformed/
* https://pypi.org/project/rapydscript/
* https://medium.com/swlh/sick-of-javascript-just-use-browser-python-4b9679efe08b
* https://github.com/yakkomajuri/brython-snake
* https://developer.chrome.com/docs/extensions/mv3/manifest/
* https://www.w3schools.com/tags/att_input_src.asp#:~:text=Definition%20and%20Usage,type%3D%22image%22%3E%20.
* https://github.com/atsepkov/RapydScript
* https://stackoverflow.com/questions/42754611/creating-and-access-a-settings-class-from-the-main-file-in-python
* https://www.youtube.com/watch?v=salY_Sm6mv4
* https://www.youtube.com/watch?v=0n809nd4Zu4&t=4s
* https://developer.chrome.com/docs/extensions/mv3/mv3-migration/
* https://www.reddit.com/r/Python/comments/pvhrvg/brython/
* https://bobbyhadz.com/blog/python-no-module-named-selenium#:~:text=The%20Python%20%22ModuleNotFoundError%3A%20No%20module,the%20pip%20install%20selenium%20command.
* https://chromedriver.chromium.org/downloads
* https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver
