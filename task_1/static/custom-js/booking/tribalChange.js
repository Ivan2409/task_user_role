/**
 * Created by oem on 2/27/17.
 */

var tribal = $('#tribal').val();

$('#tribal').on('change', function(){
    var tribal = $(this).val();
    changeSelect(tribal);
});

changeSelect(tribal);

function changeSelect(tribal_id){
    $("#city").empty();
    $.getJSON('/api/web/tribal-city/'+tribal_id, function (data) {

        $.each(data.city, function(key, val){

            $("#city")
                .append('<option value="'+val.id+'">'+val.name+'</option>');

        })


    })
}