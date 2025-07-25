function save(){

    var f_orm = '#form_task';

    var formData = $(f_orm).serialize();

    var url = $(f_orm).attr('action');    

    $.post(url, formData, function(response) {
      if (response.success){
        liveToast('bg-primary',response.message);
      } else {
        alert(response.errors);
      }
    }, 'json');
}