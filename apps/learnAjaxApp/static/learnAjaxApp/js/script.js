$(document).ready(function(){
    console.log("Document finished loading");

    $('form').submit(function(e){
        console.log("Submitting");
        e.preventDefault()
        $.ajax({
          url: '/notes',
          method: 'post',
          data: $(this).serialize(),
          success: function(serverResponse){
            console.log("Received this from server: ", serverResponse)
            $("#replace").html(serverResponse);
          }
        })
      })
})