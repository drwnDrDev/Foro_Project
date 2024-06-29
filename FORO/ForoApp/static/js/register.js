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
ver.addEventListener('mousedown', ()=>{
        rPdws.type='text'
        ver.classList.remove('i-unseen')
        ver.classList.add('i-ver')       
    })
    
ver.addEventListener('mouseup', ()=>{
        rPdws.type='password'
        ver.classList.remove('i-ver')
        ver.classList.add('i-unseen')       
    })