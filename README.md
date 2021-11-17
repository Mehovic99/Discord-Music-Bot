# The song MONKE BOT
This BOT was created with the intention to play music on Discord's voice channels by taking the YouTube URL of the song that you want and playing it for you

## How it Works?

There are three classes: Main, Song and keep_alive

### Main class

![main class](https://user-images.githubusercontent.com/76923830/142286948-d806e4ab-20f8-48f1-b516-b0575eb3379f.JPG)

The above image shows the Main class that I have built. I used Discord Development commanad cogs in order to import the
commands that I have set for my bot inside the main class so that it can be executed on launch. Seocond, I defined
within the client the prefix that the Bot should use in order to execute its commands that have been set in the class Song.
The client is used to initiate the BOT with the said commands

**UPDATE:** I have imported flask in order to create a temporary testing server to see how the bot will handle on a discord server.
The class that implements this feature is the new class called **keep_alive**

### Song class

![Song class](https://user-images.githubusercontent.com/76923830/142196941-7d791804-f926-478c-a5c5-505412fa6362.JPG)

The above image shows the Song class. Its nothing advanced. Just used YouTube Development (DL) in order to be able
to process the song with the commands that I have written. All the commands have been fixed, meaning that now all the 4 commmands
that the BOT has are working accordingly. The toast message has been fixed to now display a message once the commands has been executed
to ensure that the bot is indeed working properly.

### Keep Alive class

