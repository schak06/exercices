'use strict'

const form = document.getElementById('search-form');
const resultsContainer = document.getElementById('results');


form.addEventListener('submit', async function (event) {
  event.preventDefault();

  const query = document.getElementById('query').value;

  try {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`);
    if (!response.ok) throw new Error('Failed to fetch data.');

    const data = await response.json();


    resultsContainer.innerHTML = '';


    data.forEach(tvShow => {
      const { name, url, image, summary } = tvShow.show;


      const article = document.createElement('article');


      const title = document.createElement('h2');
      title.textContent = name;
      article.appendChild(title);


      const link = document.createElement('a');
      link.href = url;
      link.textContent = 'Details';
      link.target = '_blank';
      article.appendChild(link);


      if (image?.medium) {
        const img = document.createElement('img');
        img.src = image.medium;
        img.alt = name;
        article.appendChild(img);
      }


      if (summary) {
        const summaryDiv = document.createElement('div');
        summaryDiv.innerHTML = summary;
        article.appendChild(summaryDiv);
      }


      resultsContainer.appendChild(article);
    });
  } catch (error) {

    console.error('Error fetching data:', error);
    resultsContainer.textContent = `Error: ${error.message}`;
  }
});