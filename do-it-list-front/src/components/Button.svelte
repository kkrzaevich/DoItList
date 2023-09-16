<script>
    export let text="button"
    export let clickFunction = () => {}
</script>

<button on:click={clickFunction}>
    <p>{text}</p>
</button>

<style>
    button {
        display: flex;
        padding: 1em 4rem;
        justify-content: center;
        align-items: center;
        gap: 0.625rem;
        align-self: stretch;
        background: var(--colored, #554E4E);
        width: 100%;

        transition: box-shadow 0.25s;
    }

    button:hover {
        box-shadow: 0px 4px 12px 0px rgba(255, 255, 255, 0.25) inset, 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
    }

    button:hover > p {
        color: var(--white, #FFF);
        /* Large-bold */
        font-family: Lekton;
        font-size: 24px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
    }

    p {
        color: var(--white, #FFF);
        /* Large */
        font-family: Lekton;
        font-size: 24px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
</style>