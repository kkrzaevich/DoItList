<script>
    import Item from "./Item.svelte";
    import NewItem from "./NewItem.svelte";
    import { Router, Link, Route } from "svelte-routing";
    import { userName } from "../../stores";
    import { list } from "../../stores";
    import { onMount } from 'svelte';
    import { getList } from "../../stores";

    let localList = [];

    list.subscribe((list) => (localList = [...list]))

    let logoScr = "/logo.svg";
    let logoAlt = "do it list logo";
    let user = document.cookie;

    userName.subscribe((name) => {user = name})
    export let url = "";

    onMount(() => {
		getList();
        console.log(document.cookie)
	});
</script>
<main>
    <div class="subtext">
        <p class="subtext-text">You are {user}.</p>
        <Router {url}>
            <Link to="../"><p class="subtext-link">Want to log out?</p></Link>
        </Router>
    </div>
    <section>
        <div class="content">
            <img src={logoScr} alt={logoAlt}>
            <div class="list">
                <NewItem />
                <div class="items">
                    {#each localList as item}
                        <Item name={item.name} description={item.description} id={item.id} />
                    {/each}
                </div>
            </div>
        </div>
    </section>
</main>



<style>
    main {
        display: flex;
        padding: 32px;
        flex-direction: column;
        align-items: flex-start;
        flex: 1 0 0;
    }

    section {
        display: flex;
        padding: 44px 50px;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 10px;
        align-self: stretch;
    }
    
    .content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 70px;
        align-self: stretch;
        filter: drop-shadow(0px 4px 100px rgba(0, 0, 0, 0.05));
    }

    .list {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        gap: 40px;
        align-self: stretch;
    }

    .items {
        display: flex;
        align-items: center;
        align-content: center;
        gap: 40px;
        align-self: stretch;
        flex-wrap: wrap;
    }

    img {
        width: 500px;
    }

    .subtext {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        gap: 10px;
    }

    .subtext-text {
        color: var(--black, #000);
        /* Medium-bold */
        font-family: Lekton;
        font-size: 24px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
    }

    .subtext-link {
        color: var(--black, #000);
        /* Medium */
        font-family: Lekton;
        font-size: 24px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;

        transition: text-shadow 0.5s;
    }

    .subtext-link:hover {
        text-shadow: 0px 0px 20px rgba(0, 0, 0, 0.5);
    }
</style>

