onmouseup = function (e) {

    fetch('/mindmap/addnode_put/', {
        method: 'POST',

        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "mousex": e.clientX, "mousey": e.clientY })
    })
        .then(response => { location.reload() })
    console.log("mouse location:", e.clientX, e.clientY);

    return
}