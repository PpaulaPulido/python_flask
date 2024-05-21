$(document).ready(function(){
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
