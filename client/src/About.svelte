<script>
    import {userStore} from "./store.js"
    import {getContext, setContext} from "svelte";
    import AboutChildA from "./AboutChildA.svelte";
    import AboutChildB from "./AboutChildB.svelte";

    let user = {}

    userStore.subscribe(data => {
        user = data
    })

    console.log("userStore", userStore)

    const recordList = getContext("recordList")
    console.log("다른페이지", recordList)
    setContext("aboutA", 1)
</script>

<main>
    <h1>About</h1>
    <p>name : {user.name}</p>
    <p>email : {user.email}</p>
    <p>age : {user.age}</p>
    <AboutChildA />
    <AboutChildB />
</main>