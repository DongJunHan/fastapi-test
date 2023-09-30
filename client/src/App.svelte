<script>
	import {recordListStore} from "./store.js"

	let offset = 1
	let limit = -1
	let type = ""

    $: recordListPromise = fetch(`https://dev.braydenlab.com/api/record-list/?offset=${offset}&limit=${limit}`,{
        method : "GET",
        headers: {
            Authorization : localStorage.getItem("accessToken")
        }
    }).then(response => response.json().then(response => {
		recordListStore.set(response) //store를 사용할 경우를 상상했다.
        return type === "" ? response : filterMannequinType(response, type)
    }))

	const filterMannequinType = (data, type) => {
		let recordList = []
		for (let i = 0; i < data.length; i++) {
			if (data[i].Custom.TrainCourse.Target === type) {
				recordList.push(data[i]);
			}
		}
		return recordList
	}

	const handler = (e) => {
		type = e.target.value
	}

</script>
<main>
	<header>
		<h1>Record</h1>
	</header>
	<select on:change={handler} name="type">
		<option value="" selected>-- 마네킹 선택 --</option>
		<option value="adult">adult</option>
		<option value="child">child</option>
		<option value="infant">infant</option>
	</select>
	<div class="main" id="main" >
		{#await recordListPromise}
			<p>...Loading</p>
		{:then recordListPromise}

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

				{#each recordListPromise as record}
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

		{:catch error}
			<p>오류가 발생했습니다.</p>
		{/await}
	</div>
</main>
<style>

</style>