const pdws =document.getElementById('password')
const rPdws=document.getElementById('r-password')
const ver =document.querySelectorAll('.password')

rPdws.addEventListener('keyup',()=>{
    if(pdws.value===rPdws.value){
        
        rPdws.classList.remove('incorrect')
        rPdws.classList.add('correct')
    }else {
        rPdws.classList.remove('correct')
        rPdws.classList.add('incorrect')
    }
})


ver.forEach((element)=>{
    let campo = element.childNodes[1].childNodes[1]
    let mostrar=element.childNodes[1].childNodes[3]  
    element.addEventListener('mousedown',()=>{
            campo.type='text'        
            mostrar.classList.remove('i-unseen')
            mostrar.classList.add('i-ver')
    })
    element.addEventListener('mouseup',()=>{
        campo.type='password'
        mostrar.classList.remove('i-ver')
        mostrar.classList.add('i-unseen') 
    })  
})

// function show_password(campo){
//         campo.type='text'
//         ver.classList.remove('i-ver')
//         ver.classList.add('i-unseen') 
//      }
// ver.addEventListener('mousedown', show_password(e.target))

// ver.addEventListener('mouseup', ()=>{
//         rPdws.type='password'
//         ver.classList.remove('i-ver')
//         ver.classList.add('i-unseen')       
//     })