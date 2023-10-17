let show = document.querySelector('#show');

show.addEventListener('click', function() {
    $.ajax({
        type : 'GET',
        url : 'https://jsonplaceholder.typicode.com/todos',
        // dataType : 'json'
    }).done(function (result) {
        // console.log(result)
        let table = "";
        for (let i in result) {
            table +="<tr>"
            table += "<td>" + result[i].userId + "</td>"
            table += "<td>" + result[i].title + "</td>"
            table += "<td>" + result[i].completed + "</td>"
            table += "</tr>"
        }
        document.querySelector('tbody').innerHTML += table
    })
})
