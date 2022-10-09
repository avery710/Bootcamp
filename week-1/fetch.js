url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

function appendElem(parentElem, index, posts){
    let grid = document.createElement('div')
    parentElem.appendChild(grid)

    let img_url = posts[index]["file"].match(/(http(s?):)([/|.|\w|\s|-])*\.(?:jpg|JPG|png)/g)
    let img = document.createElement('img')
    img.src = img_url[0]

    let title = document.createElement('p')
    title.textContent = posts[index]["stitle"]

    grid.appendChild(img)
    grid.appendChild(title)

    return grid
}


fetch(url)
    .then(res => {
        return res.json()
    }).then(data => {
        let posts = data["result"]["results"]
        console.log(posts.length)

        // promotion section elements add
        let promotions = document.querySelector('.promotion-section')

        for (let i = 0; i < 2; i++){
            let per_promo = appendElem(promotions, i, posts)
            per_promo.className = "promotion"
        }

        // grid section elements add
        let grids = document.querySelector('.pic-section')

        for (let i = 2; i < 10; i++){
            let per_grid = appendElem(grids, i, posts)
            per_grid.className = "per-grid"
        }

        // load more
        let loadMore = document.querySelector('#load-more')
        let currentItems = 10

        loadMore.onclick = () => {
            for (let i = currentItems; i < currentItems + 8; i++){
                if (i >= posts.length){
                    loadMore.remove()
                    break
                }

                let per_grid = appendElem(grids, i, posts)
                per_grid.className = "per-grid"
            }

            currentItems += 8
            console.log(`current items: ${currentItems}`)
        }

    }).catch(error => {
        console.log(`error: ${error}`)
    })