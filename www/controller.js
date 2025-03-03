$(document).ready(function () { //jquery

  //Display the spoken text by us
  eel.expose(DisplayMessage);
  function DisplayMessage(message) {
    $(".siri-message li:first").text(message);
    $(".siri-message").textillate("start"); //Library used to display text animation
  }

  //After jarvis speak the text, return to the original display hood function
  eel.expose(showHood);
  function showHood() {
    $("#Oval").attr("hidden", false); //after displaying message, exit to display screen
    $("#SiriWave").attr("hidden", true);
  }
});
