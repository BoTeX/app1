$(document).ready(function(){
  $("#id_photo").attr("value", "                               link");
  $("#slideshow > div:gt(0)").hide();
  setInterval(function() { 
    $('#slideshow > div:first')
      .fadeOut(3000)
      .next()
      .fadeIn(3000)
      .end()
      .appendTo('#slideshow');
  },  12000);
});
$( "#id_photo" ).focus(function(){
  $("#id_photo").attr("value", "");
});
$( "button" ).mousedown(function() {
  $("#id_photo").attr("value", "");
  return true;
});