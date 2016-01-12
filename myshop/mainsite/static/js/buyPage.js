var tempText;
$( ".container" ).hover(
  function() {
    tempText = $("span", this).text();
    $("span", this).text("");
    if(tempText === "Estate")
      $( this ).addClass( "myClass1" );
    else if(tempText === "Transport")
      $( this ).addClass( "myClass2" );
    else if(tempText === "Electronics")
      $( this ).addClass( "myClass3" );
    else if(tempText === "Stuff")
      $( this ).addClass( "myClass4" );
    else if(tempText === "Services")
      $( this ).addClass( "myClass5" );
  }, function() {
    if(tempText === "Estate")
      $( this ).removeClass( "myClass1" );
    else if(tempText === "Transport")
      $( this ).removeClass( "myClass2" );
    else if(tempText === "Electronics")
      $( this ).removeClass( "myClass3" );
    else if(tempText === "Stuff")
      $( this ).removeClass( "myClass4" );
    else if(tempText === "Services")
      $( this ).removeClass( "myClass5" );
    $("span", this).text(tempText);
    tempText = '';
  }
);