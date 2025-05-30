#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) return console.error(error);

  const film = JSON.parse(body);
  const characters = film.characters;

  printCharacters(characters, 0);
});

function printCharacters(list, index) {
  if (index >= list.length) return;

  request(list[index], (err, res, body) => {
    if (!err) {
      const character = JSON.parse(body);
      console.log(character.name);
      printCharacters(list, index + 1);
    } else {
      console.error(err);
    }
  });
}
