var discuss = function(){
    var topic = $('#topic').val();
    $('#romney').load('romneySay?topic=' + topic);
    $('#obama').load('obamaSay?topic=' + topic);
};

$(document).ready(function() {
    $('#discuss').click(discuss);
});

