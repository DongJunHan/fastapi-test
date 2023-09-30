<script>
    import {recordListStore} from "./store.js"

    let recordList = $recordListStore


    function getFilteredResultListBy(type) {

        const result = $recordListStore.filter(values => {
            return values.Custom.TrainCourse.Target === type
        })

        // for (let i = 0; i < $recordListStore.length; i++) {
        //     console.log("$recordListStore[i].Custom.TrainCourse.Target", $recordListStore[i].Custom.TrainCourse.Target)
        //     if ($recordListStore[i].Custom.TrainCourse.Target === type) {
        //         result.push($recordListStore[i]);
        //     }
        // }
        return result
    }

    const filterMannequinType = (type) => {
        recordList = getFilteredResultListBy(type)
    }

    const handler = (e) => {
        console.log("handler")
        filterMannequinType(e.target.value)
    }
</script>

<main>
    <h1>Record</h1>
    <div class="mb-3">
        <label for="exampleFormControlInput1" >Email address</label>
        <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
    </div>
    <div class="mb-3">
        <label for="exampleFormControlTextarea1" class="form-label">Example textarea</label>
        <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
    </div>
    <select on:change={handler} name="type">
        <option value="" selected>-- 마네킹 선택 --</option>
        <option value="adult">adult</option>
        <option value="child">child</option>
        <option value="infant">infant</option>
    </select>
    <div class="w-100 border">
        <div class="row border-bottom">
            <div class='col-2'>날짜</div>
            <div class='col-2'>훈련유형</div>
            <div class='col-2'>이메일</div>
            <div class='col-2'>이름</div>
            <div class='col-2'>인증서</div>
            <div class='col-1'>점수</div>
            <div class="col-1">타입</div>
        </div>

        {#each recordList as record}
            <div class="row">
                <div class="col-2">{record.Usage.Date}</div>
                <div class="col-2">{record.Usage.Type}</div>
                <div class="col-2">{record.Usage.Email}</div>
                <div class="col-2">{record.Usage.uSername} {record.Usage.uName}</div>
                <div class="col-2">{record.ResultSummary.JudgResult}</div>
                <div class="col-1">{record.ResultByCycle.ScoreByCycle.Overall}</div>
                <div class="col-1">{record.Custom.TrainCourse.Target}</div>
            </div>
        {/each}
    </div>
</main>