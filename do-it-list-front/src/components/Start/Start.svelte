<script>
    import { Router, Link, Route } from "svelte-routing";
    import Button from "../Button.svelte";

    let logoScr = "/logo.svg";
    let logoAlt = "do it list logo";

    export let url = "";
</script>

<main>
    <section>
        <img src={logoScr} alt={logoAlt}>
        <Router {url}>
            <nav>
              <Link to="/login"><Button text={"Log in"} /></Link>
              <Link to="/signup"><Button text={"Sign up"} /></Link>
            </nav>
        </Router>
    </section>
</main>

<style>
    main {
        display: flex;
        padding: 100px 529px;
        justify-content: center;
        align-items: flex-start;
        align-content: flex-start;
        gap: 10px;
        flex-wrap: wrap;
        background: var(--white, #FFF);
    }

    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 70px;


        filter: drop-shadow(0px 4px 100px rgba(0, 0, 0, 0.05));
    }

    nav {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: stretch;
        gap: 25px;
    }

    img {
        width: 500px;
    }
</style>
