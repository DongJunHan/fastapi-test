<script>
    import {numStore} from "./store.js";

    let num = 0

    console.log("numStore", numStore)

    numStore.subscribe((data) => {
        num = data
    })

    numStore.set(23)

    numStore.update((data) => {
        return data + 1
    })

    $numStore = 50
</script>


<main>
    <p>store number : {num}</p>
</main>