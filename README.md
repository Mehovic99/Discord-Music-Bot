# The song MONKE BOT
This BOT was created with the intention to play music on Discord's voice channels by taking the YouTube URL of the song that you want and playing it for you

## How it Works?

There are two classes: Main and Song

### Main class

![Main class](https://user-images.githubusercontent.com/76923830/142169494-745916e2-c087-4b18-ab0e-0fd3f16b53e8.JPG)

The above image shows the Main class that I have built. I used Discord Development commanad cogs in order to import the
commands that I have set for my bot inside the main class so that it can be executed on launch. Seocond, I defined
within the client the prefix that the Bot should use in order to execute its commands that have been set in the class Song.
The client is used to initiate the BOT with the said commands

### Song class

![Song class](https://user-images.githubusercontent.com/76923830/142196941-7d791804-f926-478c-a5c5-505412fa6362.JPG)

The above image shows the Song class. Its nothing advanced. Just used YouTube Development (DL) in order to be able
to process the song with the commands that I have written. All the commands have been fixed, meaning that now all the 4 commmands
that the BOT has are working accordingly. The toast message has been fixed to now display a message once the commands has been executed
to ensure that the bot is indeed working properly.
