function save() {
    var f_orm = '#form_task';
    var formElement = $(f_orm)[0];

   
    if (!formElement.reportValidity()) { // Exibe os balões de erro se houver campos inválidos
        return; // Não envia se o formulário estiver inválido
    }

    var formData = $(f_orm).serialize();
    var url = $(f_orm).attr('action');    

    $.post(url, formData, function(response) {
        if (response.success) {
            liveToast('bg-primary', response.message);           
             window.location.href = `/print/print_form/${response.message}/`;


        } else {
            liveToast('bg-warning', response.message);
        }
    }, 'json');
}