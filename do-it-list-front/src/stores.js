import { writable } from 'svelte/store';

export const list = writable([]);
export const userName = writable("Oleg");

export async function getList () {
    try {
        const response = await fetch('http://localhost:8080/list/get', {method: 'GET'})
        list.set(await response.json())
    } catch(err) {
        throw new Error(err.message)
    }
}

export async function addItem (item) {
    try {const res = await fetch('http://localhost:8080/list/add', {
        method: 'POST',
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(item),
    })
} catch(err) {
        alert(err.message)
    }
}

export async function deleteItem (itemId) {
    try {const res = await fetch('http://localhost:8080/list/delete', {
        method: 'DELETE',
        mode: "cors",
        body: itemId,
    })
} catch(err) {
        alert(err.message)
    }
}

export async function editItem (item) {
    try {const res = await fetch('http://localhost:8080/list/edit', {
        method: 'POST',
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(item),
    })
} catch(err) {
        alert(err.message)
    }
}



