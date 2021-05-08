fetch('https://dummyapi.io/data/api/user').then(
  resp => resp.json() // this returns a promise
).then(repos => {
  console.log(repos)
  mydata(repos)
}).catch(err => {
  console.log(err);})

  const showData = document.getElementById('datashow')

function mydata(data){
    for (var i = 0; i < data.length; i++) {
        // append each person to our page
        showData.innerHTML=`<p>${data.firstName}</p>`
      }

}
