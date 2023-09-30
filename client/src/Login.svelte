<script>
    let clientId;
    let password;

    const clientLogin = async () =>{
        const response = await fetch('http://127.0.0.1:5000/api/new/auth/client/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                clientID: clientId,
                passcode: password,
            }),
        })
        console.log("response", response)
        if(response.ok){
            const result = await response.json()
            localStorage.setItem("accessToken", result.access_token)
            console.log("result", result)
            window.location.href = "/#/home"
        }

    }
    const handleSubmit = () => {
        console.log(clientId, password)
        clientLogin()
    }
</script>

<main>
    <h1>Login</h1>
    <div>
        <form on:submit|preventDefault = {handleSubmit}>
            <div>Client ID</div>
            <input type="text" placeholder="clientId" bind:value={clientId}>
            <div>Password</div>
            <input type="password" placeholder="password" bind:value={password}>
            <div>
                <button>로그인</button>
            </div>
        </form>
    </div>
</main>