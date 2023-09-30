import {writable, readable} from "svelte/store";

const numStore = writable(0)

const userStore = readable({
    name : "글랜",
    email : "glenn@innosonian",
    age : "38",
})

const recordListStore = writable([])

export {numStore, userStore, recordListStore}