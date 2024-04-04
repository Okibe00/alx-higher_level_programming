/*
Write a JavaScript script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header

You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your brows
*/
$('#update_header').bind('click', function () {
  const header = $('header');
  header.text('New Header');
});
