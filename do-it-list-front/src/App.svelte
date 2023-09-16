<script>
  import { Router, Link, Route } from "svelte-routing";
  import Login from "./components/Login/Login.svelte";
  import Singup from "./components/Signup/Singup.svelte";
  import Start from "./components/Start/Start.svelte";
  import Todolist from "./components/Todolist/Todolist.svelte";

  export let url = "";
</script>

<Router {url}>
    <Route path="/login" component={Login} />
    <Route path="/signup" component={Singup} />
    <Route path="/todolist" component={Todolist} />
    <Route path="/"component={Start} />
</Router>

<style>
</style>
