<script>
    import Router from "svelte-spa-router";
    import App from "./App.svelte"
    import Home from "./Home.svelte"
    import Login from "./Login.svelte"

    const routes = {
        '/': Login,
        '/home': Home,
        '/record': App,
    };

    const logout = () => {
        console.log("logout!!")
        localStorage.removeItem("accessToken")
        window.location.href = "/"
    }
</script>

<main>
    <nav>
        <a href="#/">학생 로그인</a>
        <a on:click={logout}>로그아웃</a>
        <a href="#/home">홈</a>
        <a href="#/record">훈련기록</a>
    </nav>
    <Router {routes}/>
</main>


<style>
    a {
        text-decoration: none !important;
    }
</style>