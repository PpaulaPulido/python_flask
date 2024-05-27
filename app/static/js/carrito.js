$(document).ready(function(){

    $('.delete-icon').on('click', function() {
        const itemId = $(this).data('id');
        $.post('/eliminar-del-carro', { idcan: itemId }, function(data) {
            alert(data.message || "Canción eliminada del carro.");
            location.reload(); // Recargar la página para actualizar el carrito visualmente
        });
    });

    $('.deleteAll').on('click', function() {
        const itemId = $(this).data('id');
        $.post('/eliminar-del-carro', function(data) {
            alert(data.message || "Canciones eliminadas del carro.");
            location.reload(); // Recargar la página para actualizar el carrito visualmente
        });
    });

    $('.agregarCan').on('click',function(){
        const idcan = $(this).data('id');
        const titulocan = $(this).data('titulo');
        const preciocan = $(this).data('precio');

        $.post('/Adicionarcarrito',{
            idcan: idcan,
            titulocan:titulocan,
            preciocan:preciocan
        }, function(data){
            alert(data.message || 'cancion agregada')
        });
    });
});
