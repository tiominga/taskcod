function form_fetch(reset_offset = false) {

    if (reset_offset) { stt_offset.value = 0; }
    f_orm = document.getElementById("form_query");
    formData = new FormData(f_orm);
    const csrfToken = formData.get('csrfmiddlewaretoken');
    const url = f_orm.action;

    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken
        },
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.status == 'success') {
                document.getElementById("dv_data").innerHTML = data.table;
            } else {
                alert(data.message);
            }
        })

}

function edit_task(id, event) {

    event.stopPropagation();
    alert("Edit function is not implemented yet. id: " + id);


}

function delete_task(id, event) {

    event.stopPropagation();
    alert("Delete function is not implemented yet. id: " + id);

}

function tr_click(id, event) {

    event.stopPropagation();
    document.getElementById('ed_id_task').value = id;
    document.getElementById('dv_data_change').style.display = 'Block';

}

function change_priority() {

    let id = document.getElementById('ed_id_task').value;
    let priority = document.getElementById('prioridade').value;
    document.getElementById('dv_data_change').style.display = 'None';

    let url = `/task/task_change_priority/${id}/${priority}/`;

    fetch(url, {
        method: 'GET'
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            liveToast('bg-primary', data.message)

        })
        .catch(error => console.error(error));


}





