<script>
    import { deleteItem } from "../../stores";
    import { getList } from "../../stores";

    export let name="Eat";
    export let itemId="1";
    export let description="I need to eat surströmming today";

    const pressDelete = () => {
        deleteItem(
            itemId
        ).then(getList)
    }
</script>

<main>
    <h1>{name}</h1>
    <p>{description}</p>
    <div>
        <button on:click={() => {}}>
            <img class="edit" src="/edit.svg" alt="edit item">
        </button>
        <button on:click={pressDelete}>
            <img class="delete" src="/delete.svg" alt="delete item">
        </button>
    </div>
</main>

<style>
    main {
        display: flex;
        min-width: 350px;
        max-width: 800px;
        padding: 25px 25px;
        flex-direction: column;
        align-items: flex-start;
        gap: 25px;
        flex: 1 0 0;
        border-radius: 25px;
        border: 1px solid var(--black, #000);
        background: var(--white, #FFF);
    }

    h1 {
        align-self: stretch;
        color: var(--black, #000);
        /* Large-bold */
        font-family: Lekton;
        font-size: 24px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
    }

    p {
        align-self: stretch;
        color: var(--black, #000);
        /* Medium */
        font-family: Lekton;
        font-size: 18px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }

    div {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 18px;
        align-self: stretch;
    }

    .edit {
        width: 32px;
        height: 32px;
        fill: var(--black, #000);
    }

    .delete {
        width: 28.444px;
        height: 32px;
        fill: var(--black, #000);
    }
</style>