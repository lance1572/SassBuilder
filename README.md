# SassBuilder
Sublime Text Package for Dart Sass. 

This is a Sublime plugin to compile your Sass using Dart Sass. This is my first attempt at creating a plugin and I'm sure that there are somethings to be improved upon. This is for Mac but i'm sure it could work for Windows and Linux with some path adjustments. So be forewarned. 

For this, I used the Dart Sass exec instead of the other install methods like brew or npm - I needed something very quick. Later, I will change to something more programatic.

**I am not supporting this so use at your own risk. It may OR may not work for you.**

## Mac

*This is an unzipped package which goes into the Sublime Text Packages folder. Dump the folder in there and restart ST*

`Library/Application Support/Sublime Text/Packages/`

- Download Dart Sass https://github.com/sass/dart-sass/releases
- Move to preferred directory
- Add the location to the executable to the settings file `SassBuilder.sublime-settings`
- Make a input folder in your project (name it sass, scss or whatever)
- Create a .scss file in that input folder and add some sass to it, save
- Add that input folder name in the previous step to the settings file `SassBuilder.sublime-settings`
- Add the output folder name to the setting file `SassBuilder.sublime-settings`
- Go to Tools > Build
