<template>
  <div class="form">
    <form v-on:submit="handleLogin">
      <b-form-group
        id="input-group-1"
        label="Email address:"
        label-for="input-1"
        description=""
      >
        <b-form-input
          id="input-1"
          v-model="email"
          type="text"
          required
          placeholder="Enter email"
        ></b-form-input>
      </b-form-group>
      <b-form-group>
        <label for="text-password">Password</label>
        <b-input
          type="password"
          id="text-password"
          v-model="password"
          aria-describedby="password-help-block"
          placeholder="Password"
        ></b-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Login</b-button>
    </form>
  </div>
</template>
""
<script>
import { mapActions } from "vuex";

export default {
  name: "LoginForm",
  data() {
    return {
      email: "",
      password: "",
      nextPath: "/feed",
      errorMessage: "",
    };
  },
  mounted() {
    this.updateAfterLoginNextPath();
  },
  methods: {
    handleLogin(event) {
      event.preventDefault();
      this.login({ email: this.email, password: this.password }).then(() => {
        this.$router.push(this.nextPath);
      });
    },
    updateAfterLoginNextPath() {
      if ("next" in this.$route.query) {
        this.nextPath = this.$route.query.next;
      }
    },
    ...mapActions(["login"]),
  },
};
</script>

<style scoped>
form {
  max-width: 400px;
  margin: 0 auto;
}
</style>
