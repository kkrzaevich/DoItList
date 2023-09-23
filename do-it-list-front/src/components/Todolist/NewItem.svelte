<script>
    import { addItem } from "../../stores";
    import { getList } from "../../stores";
    import AddIcon from "./AddIcon.svelte";
    import { fade } from 'svelte/transition';

    let name;
    let itemId;
    let description;

    const pressAdd = () => {
        addItem({
            name,
            description,
            itemId
        }).then(getList)
    }

    let toggle = false;
</script>

<main>
    {#if (toggle === false)}
        <button class="open-container"  in:fade={{ duration : 500 }}  out:fade={{ duration : 500 }} on:click={() => {toggle = true}}>
            <AddIcon color="black" />
        </button>
    {:else}
        <section in:fade={{ duration : 500 }}  out:fade={{ duration : 500 }}>
            <div class="header">
                <div class="title">
                    <h1>Title:</h1>
                    <input type="text" bind:value={name} placeholder="Write here..."/>
                </div>
                <button class="hide-container" on:click={() => {toggle = false}}>
                    <img class="hide" src="/hide.svg" alt="hide item">
                </button>
            </div>
            <div class="description">
                <h1>Description:</h1>
                <input type="text" bind:value={description} placeholder="Write here..."/>
            </div>
            <button class="add-container" on:click={pressAdd}>
                <AddIcon color="white" />
            </button>
        </section>
    {/if}
</main>


<style>


    main {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        gap: 25px;
        align-self: stretch;
    }

    .open-container {
        display: flex;
        padding: 0px 30px;
        justify-content: flex-end;
        align-items: center;
        align-self: stretch;
    }

    section {
        display: flex;
        min-width: 400px;
        padding: 25px 20px;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        gap: 25px;
        align-self: stretch;
        border-radius: 25px;
        border: 1px solid var(--white, #FFF);
        background: var(--colored, #554E4E);
    }

    .header {
        display: flex;
        align-items: flex-start;
        gap: 25px;
        align-self: stretch;
    }

    .title {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
        flex: 1 0 0;
        align-self: stretch;
    }

    .title > h1 {
        align-self: stretch;
        color: var(--white, #FFF);
        /* Large-bold */
        font-family: Lekton;
        font-size: 24px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
    }

    .title > input {
        align-self: stretch;
        color: var(--white, #FFF);
        /* Large */
        font-family: Lekton;
        font-size: 24px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }

    .hide-container {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 18px;
    }

    .hide {
        width: 48px;
        height: 48px;
    }

    .description {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
        align-self: stretch;
    }

    .description > h1 {
        align-self: stretch;
        color: var(--white, #FFF);
        /* Medium-bold */
        font-family: Lekton;
        font-size: 18px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
    }

    .description > input {
        align-self: stretch;
        color: var(--white, #FFF);
        /* Medium */
        font-family: Lekton;
        font-size: 18px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }

    .add-container {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 18px;
        align-self: stretch;
    }

    input {
        transition: filter 0.5s;
    }

    input:hover {
        filter: drop-shadow(0px 0px 8px rgba(255, 255, 255, 1));
    }

    button {
        transition: filter 0.25s;
    }

    button:hover {
        filter: drop-shadow(0px 0px 5px rgba(255, 255, 255, 1));
    }

</style>