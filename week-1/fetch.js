url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

fetch(url)
    .then(res => {
        return res.json()
    }).then(data => {
        console.log(data["result"]["results"])
    }).catch(error => {
        console.log(`error: ${error}`)
    })