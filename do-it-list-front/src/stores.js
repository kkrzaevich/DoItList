import { writable } from 'svelte/store';

export const list = writable([]);
export const userName = writable(document.cookie);

export async function getList () {
    try {const res = await fetch('http://localhost:8080/items', {
        credentials:'include',
        method: 'GET',
        mode: "cors",
    })

    if (!res.ok) {
        throw new Error(`An error has occured: ${res.status}`)
    } else {
        list.set(await res.json())
    }

} catch(err) {
        throw new Error(`An error has occured: ${err.message}`)
    }
    
}

export async function addItem (item) {
    try {const res = await fetch(`http://localhost:8080/items/`, {
        credentials:'include',
        method: 'POST',
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(item),
    })

    if (!res.ok) {
        throw new Error(`An error has occured: ${res.status}`)
    } else {
        getList()
    }
} catch(err) {
        throw new Error(`An error has occured: ${err.message}`)
    }
}

export async function deleteItem (id) {
    try {const res = await fetch(`http://localhost:8080/items/${id}`, {
        credentials:'include',
        method: 'DELETE',
        mode: "cors",
        // headers: {
        //     "Content-Type": "application/json",
        // },
        // body: JSON.stringify({
        //     id: id
        // }),
    })

    if (!res.ok) {
        throw new Error(`An error has occured: ${res.status}`)
    } else {
        getList()
    }
} catch(err) {
        alert(err.message)
    }
}

export async function editItem (item) {
    try {const res = await fetch(`http://localhost:8080/items/${item.id}`, {
        credentials:'include',
        method: 'PUT',
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(item),
    })

    if (!res.ok) {
        throw new Error(`An error has occured: ${res.status}`)
    } else {
        getList()
    }
} catch(err) {
        throw new Error(`An error has occured: ${err.message}`)
    }
}



