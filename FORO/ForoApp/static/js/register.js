const pdws =document.getElementById('password')
const rPdws=document.getElementById('r-password')
const ver =document.getElementById('ver')

rPdws.addEventListener('keyup',()=>{
    if(pdws.value===rPdws.value){
        
        rPdws.classList.remove('incorrect')
        rPdws.classList.add('correct')
    }else {
        rPdws.classList.remove('correct')
        rPdws.classList.add('incorrect')
    }
})
ver.addEventListener('click', ()=>{
    if(rPdws.type==='password'){
        ver.classList.remove('unseen')
        ver.classList.add('show')
        rPdws.type='text'
    }else{
        ver.classList.remove('show')
        ver.classList.add('unseen')
        rPdws.type='text'
    }
})