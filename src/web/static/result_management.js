$(document).ready(function () {
    function delete_result() {
        if (! confirm('Are you sure you want to delete ' + this.id + ' result?')){
            return;
        }
        var obj = this;
        $.post(('results/delete/' + this.id), function (data, status) {
            console.log('data:' + data.Message);
            $(obj).parents('tr').remove();
        }).fail(function (data, status) {
            alert(data.responseText);
            console.log('FAIL');
            console.log('data: ' + data.status);
            console.log('status: ' + status);
        });

    }

    $(".btn-delete").click(delete_result);
});
