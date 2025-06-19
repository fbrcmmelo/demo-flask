const PATH = "/users";
const HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

async function addUser() {
    const username = document.getElementById("addUsername").value;
    const email = document.getElementById("addEmail").value;
    const body = JSON.stringify({username: username, email: email});

    const response = await fetch(PATH, {
        method: "POST",
        headers: HEADERS,
        body: body
    });

    alert(await response.text());
    
    location.reload();
}

async function deleteUser() {
    const userId = document.getElementById("deleteUserId").value;
    const response = await fetch(PATH + `/${userId}`, {
        method: "DELETE",
        headers: HEADERS,
    });

    alert(await response.text());

    location.reload();
}