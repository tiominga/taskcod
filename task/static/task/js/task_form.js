// Pega o valor do cookie csrftoken
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// Configura o jQuery para enviar o token CSRF em requisições POST, PUT, DELETE etc
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!/^GET|HEAD|OPTIONS|TRACE$/i.test(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        }
    }
});

function save() {
    var f_orm = '#form_task';
    var formData = $(f_orm).serialize();
    var url = $(f_orm).attr('action');    

    $.post(url, formData, function(response) {
        if (response.success === 'true') {
            liveToast('bg-primary', response.message);
            // Redireciona para a página print_form com o id da task
            window.location.href = '/print/print_form/' + response.task_id + '/';
        } else {
            liveToast('bg-warning', response.message);
        }
    }, 'json');
}
