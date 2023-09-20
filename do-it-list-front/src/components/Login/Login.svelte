<script>
    import { Router, Link, navigate } from "svelte-routing";

    let name = "";
    let password = "";
    let result;

	async function login () {
		try {const res = await fetch('http://localhost:8080/auth/register', {
			method: 'POST',
            mode: "cors",
            headers: {
                "Content-Type": "application/json",
            },
			body: JSON.stringify({
				name,
				password
			}),
		})

        console.log(JSON.stringify({
				name,
				password
			}))
    
        const json = await res.json()
		result = JSON.stringify(json)
    } catch(err) {
            alert(err.message)
        }
		
	}

    import Button from "../Button.svelte";

    let logoScr = "/logo.svg";
    let logoAlt = "do it list logo";

    export let url = "";
</script>

<main>
    <section>
        <img src={logoScr} alt={logoAlt}>

        <div class="main-content">
            <div class="buttons">
                <input type="text" bind:value={name} placeholder="Login"/>
                <input type="password" bind:value={password} placeholder="Password"/>
                <Button text={"Log in"} clickFunction={()=>{
                    console.log(JSON.stringify({
                        name,
                        password
                    }));
                    login().then(() => {
                        navigate("/todolist", { replace: true });
                    });
                }}/>

            </div>
            <div class="login-redirect">
                <p class="login-text">Do not have an account? &nbsp</p>
                <Router {url}>
                      <Link to="/signup"><p class="login-link">Sign up</p></Link>
                </Router>
            </div>
        </div>
    </section>
</main>

<!-- <p>Result: {result}</p> -->

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

    .main-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 50px;
    }

    .buttons {
        display: flex;
        min-width: 300px;
        max-width: 500px;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 20px;
    }

    input {
        display: flex;
        padding: 12px 30px;
        align-items: center;
        gap: 10px;
        align-self: stretch;
        border-radius: 15px;
        border: 1px solid var(--black, #000);
        background: var(--white, #FFF);
        box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);

        color: var(--black, #000);
        /* Large */
        font-family: Lekton;
        font-size: 24px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;

        transition: filter 0.25s;
    }

    input:hover {
        filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.5));
    }

    img {
        width: 500px;
    }

    .login-redirect {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .login-text {
        color: var(--black, #000);
        /* Medium */
        font-family: Lekton;
        font-size: 16px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }

    .login-link {
        color: var(--black, #000);
        /* Medium-bold */
        font-family: Lekton;
        font-size: 16px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;

        transition: filter 0.25s;
    }

    .login-link:hover {
        filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.5));
    }
</style>