/** Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

All movie titles must be list in the HTML tag UL#list_movies
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:
*/
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, statusCode) {
  const list = $('#list_movies');
  $.each(data.results, function (indx, obj) {
    const title = obj.title;
    list.append(`<li>${title}</li>`);
  });
});
