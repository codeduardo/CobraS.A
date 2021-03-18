const messageDelcategory= category =>{
    const lista = {
        'success':'Proceso Exitoso..!',
        'error': 'Oooops...!'
    }
    return lista[category]
}



function mostrarAlerta(category,message){
    Swal.fire({
        icon: category,
        title: messageDelcategory(),
        text: message,
      })
}