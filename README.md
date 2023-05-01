# MaterialSymbolsToFont
A Python script to create a font using the data downloaded from Material Symbols Github repository


To run:  

1. Install python 3.11 or newer or configure pipenv using the `Pipfile`. The project has no actual dependencies
2. Install https://github.com/tancredi/fantasticon 
3. Download the https://github.com/google/material-design-icons/tree/master/symbols/web and place it in the project directory.
  You can use `git sparse checkout set symbols/web` to reduce download size.
4. Run `main.py`
5. Follow the instructions in the terminal. Provide the topmost (`material-design-icons`) folder when prompted, not a subdirectory with symbols. 
6. Upload the font to https://android-iconics.mikepenz.com/ and download the resulting classes
7. Place the resulting class in your code
