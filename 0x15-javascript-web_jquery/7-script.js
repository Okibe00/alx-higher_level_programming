/* Write a JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

The name must be displayed in the HTML tag DIV#character
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser: */

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data, statusCode) => {
  $('#character').text(data.name);
});
