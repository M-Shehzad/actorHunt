btn = document.querySelector('.btn-div button');

actorName = document.querySelector('.search');

async function search(){
    res = await fetch('/search',{
        method:'POST',
        headers:{
            'content-type':'application/json'
        },
        body:JSON.stringify({
            actorname: actorName
        })
    })
    data = res.JSON()
    console.log(data)
}

btn.addEventListener('click',(e)=>{
    e.preventDefault();
    search();
})