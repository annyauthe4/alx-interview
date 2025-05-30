<h1> Star Wars API </h1>
The “0. Star Wars Characters” project requires you to interact with an external API to fetch
and display information about Star Wars characters based on the movie ID provided as an argument.
To successfully complete this project, you need to be familiar with several key concepts related to
web programming, API interaction, and asynchronous programming in JavaScript.

<h1> Install Node 10 </h1>
<code>
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</code>

<h1> Install semi-standard </h1>
<code>
$ sudo npm install semistandard --global
</code>

<h1> Install request module and use it </h1>
<code>
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
</code>

<h1> Tasks </h1>
Write a script that prints all characters of a Star Wars movie:

The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name per line in the same order as the “characters” list in the /films/ endpoint
You must use the Star wars API
You must use the request module
