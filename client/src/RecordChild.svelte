<script>

    import {getContext} from "svelte";
    import RecordChildB from "./RecordChildB.svelte";

    let recordList = getContext("recordList")
</script>

<main>
    <h1>RecordChild</h1>
        <ul>
            {#each recordList as item}
                <li>
                    <p>[{item.Usage.Date}] {item._id}</p>
                </li>
            {/each}
        </ul>
<!--    <RecordChildB />-->
</main>