<script>
    import {getContext, setContext} from "svelte";

    setContext("about", 1)
    let result = getContext("aboutA")
    console.log("about result", result)
</script>

<main>
    <h1>ChildA</h1>
</main>