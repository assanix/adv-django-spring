<template>
  <div class="login-container">
    <div class="login-card">
      <h2 class="title">🔐 Login</h2>
      <form @submit.prevent="handleLogin" class="login-form">
        <input v-model="username" placeholder="👤 Username" required class="input" />
        <input v-model="password" type="password" placeholder="🔑 Password" required class="input" />
        <button type="submit" class="button">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    ...mapActions(['login']),
    async handleLogin() {
      try {
        await this.login({ username: this.username, password: this.password });
        this.$router.push('/admin');
      } catch (error) {
        console.error('Login error:', error);
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: #f4f6f8;
}

.login-card {
  background: #fff;
  padding: 40px 30px;
  border-radius: 16px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
  width: 100%;
  max-width: 400px;
  text-align: center;
}

.title {
  margin-bottom: 20px;
  color: #2c3e50;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.input {
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 10px;
  font-size: 1rem;
}

.button {
  padding: 12px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.button:hover {
  background-color: #2c8c6f;
}
</style>
