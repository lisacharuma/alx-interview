#!/usr/bin/node

const axios = require('axios');
const process = require('process');

if (process.argv.length !== 3) {
    console.log("Usage: node star_wars_characters.js <Movie ID>");
    process.exit(1);
}

const movieId = process.argv[2];

const getMovieCharacters = async (movieId) => {
    try {
        // Base URL for the Star Wars API
        const baseURL = 'https://swapi.dev/api';
        
        // Fetch the movie details from the API
        const movieURL = `${baseURL}/films/${movieId}/`;
        const response = await axios.get(movieURL);
        
        // Get the list of character URLs
        const characters = response.data.characters;
        
        // Fetch and print each character's name
        for (const characterURL of characters) {
            const charResponse = await axios.get(characterURL);
            console.log(charResponse.data.name);
        }
    } catch (error) {
        console.error(`Error: Unable to fetch movie with ID ${movieId}`);
    }
};

getMovieCharacters(movieId);
