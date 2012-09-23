var discuss = function(){
    var topic = $('#topic').val();
    $('#romney').load('romneySay?topic=' + escape(topic));
    $('#obama').load('obamaSay?topic=' + escape(topic));
};

$(document).ready(function() {
    $('#discuss').click(discuss);
});
