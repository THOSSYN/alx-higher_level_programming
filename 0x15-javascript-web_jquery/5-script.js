// A  script that adds a <li> element to a list when the user clicks on the tag

$(function () {
  $('#add_item').on('click', function () {
    $('.my_list').text('<li>Item</li>');
  });
});
