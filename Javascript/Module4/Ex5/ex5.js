'use strict'

async function fetchRandomJoke() {
    try {
      const response = await fetch('https://api.chucknorris.io/jokes/random');
      if (!response.ok) throw new Error('Failed to fetch joke.');

      const data = await response.json();

      console.log('Random Chuck Norris Joke:', data.value);
    } catch (error) {

      console.error('Error fetching joke:', error);
    }
  }

  fetchRandomJoke();